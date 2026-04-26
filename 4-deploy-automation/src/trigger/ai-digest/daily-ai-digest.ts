import { schedules } from "@trigger.dev/sdk/v3";

const AI_KEYWORDS = [
  "ai", "llm", "claude", "gpt", "gemini", "anthropic", "openai",
  "nvidia", "mcp", "model", "neural", "machine learning", "transformer",
  "diffusion", "agent", "deepmind", "mistral", "groq", "hugging face",
];

const HN_BASE = "https://hacker-news.firebaseio.com/v0";
const RECIPIENT = "dlohanata@gmail.com";

type HNItem = {
  id: number;
  title: string;
  url?: string;
  score: number;
  type: string;
};

type Article = {
  title: string;
  url: string;
  text: string;
  score: number;
  source: string;
};

export const dailyAiDigest = schedules.task({
  id: "daily-ai-digest",
  cron: "0 0 * * *", // 00:00 UTC = 07:00 WIB
  retry: { maxAttempts: 2 },

  run: async () => {
    // 0. Validate secrets
    const openrouterKey = process.env.OPENROUTER_API_KEY;
    const resendKey = process.env.RESEND_API_KEY;
    const firecrawlKey = process.env.FIRECRAWL_API_KEY;
    if (!openrouterKey) throw new Error("OPENROUTER_API_KEY is not set");
    if (!resendKey) throw new Error("RESEND_API_KEY is not set");
    if (!firecrawlKey) throw new Error("FIRECRAWL_API_KEY is not set");

    const today = new Date().toLocaleDateString("en-US", {
      weekday: "long", year: "numeric", month: "long", day: "numeric",
      timeZone: "Asia/Jakarta",
    });

    console.log(`Running AI digest for ${today}`);

    // 1. Fetch Hacker News top stories filtered by AI keywords
    const topIds: number[] = await fetch(`${HN_BASE}/topstories.json`).then(r => r.json());

    const hnItems: HNItem[] = await Promise.all(
      topIds.slice(0, 100).map(id =>
        fetch(`${HN_BASE}/item/${id}.json`).then(r => r.json())
      )
    );

    const hnAiItems = hnItems
      .filter(item =>
        item?.title && item.type === "story" &&
        AI_KEYWORDS.some(kw => item.title.toLowerCase().includes(kw))
      )
      .slice(0, 10);

    console.log(`Found ${hnAiItems.length} AI-related HN stories`);

    // 2. Firecrawl web search for latest AI news
    const firecrawlRes = await fetch("https://api.firecrawl.dev/v1/search", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${firecrawlKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: "latest AI model release news today 2025",
        limit: 5,
        scrapeOptions: { formats: ["markdown"] },
      }),
    }).then(r => r.json());

    const firecrawlArticles: Article[] = (firecrawlRes.data ?? []).map((item: { title?: string; url?: string; markdown?: string; description?: string }) => ({
      title: item.title ?? "Untitled",
      url: item.url ?? "",
      text: (item.markdown ?? item.description ?? "").slice(0, 2000),
      score: 0,
      source: "firecrawl",
    }));

    console.log(`Firecrawl returned ${firecrawlArticles.length} results`);

    // 3. Fetch article bodies for HN stories
    const hnArticles: Article[] = await Promise.all(
      hnAiItems.map(async (item) => {
        const url = item.url ?? `https://news.ycombinator.com/item?id=${item.id}`;
        try {
          const html = await fetch(url, { signal: AbortSignal.timeout(8000) }).then(r => r.text());
          const text = html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim().slice(0, 2000);
          return { title: item.title, url, text, score: item.score, source: "hackernews" };
        } catch {
          return { title: item.title, url, text: "(could not fetch article body)", score: item.score, source: "hackernews" };
        }
      })
    );

    const allArticles = [...hnArticles, ...firecrawlArticles];

    // 4. Summarize with Claude
    const prompt = `You are an AI news curator. Based on the articles below, write a daily digest formatted as clean HTML (inner content only — no <html>, <head>, or <body> tags).

Structure:
1. A brief intro line for ${today}
2. <h2>Top Stories</h2> — 3 to 5 bullet points, each with a hyperlinked title and a 1-sentence summary
3. <h2>Model Releases &amp; Research</h2> — notable new models, papers, or benchmarks (skip if none)
4. <h2>Industry News</h2> — Nvidia, company moves, MCP, tooling, policy (skip if none)
5. A short sign-off line

Rules:
- Use <ul><li> for bullets
- Hyperlink every story title with its URL using <a href="URL">Title</a>
- Keep each summary to 1 sentence
- Be concise and scannable
- Skip a section entirely if there's no relevant content

ARTICLES:
${allArticles.map((a, i) => `[${i + 1}] ${a.title}\nURL: ${a.url}\nScore: ${a.score}\nSource: ${a.source}\n\n${a.text}`).join("\n\n---\n\n")}`;

    const claudeRes = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${openrouterKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "google/gemini-2.0-flash-001",
        max_tokens: 1500,
        messages: [{ role: "user", content: prompt }],
      }),
    }).then(r => r.json());

    console.log("OpenRouter raw response:", JSON.stringify(claudeRes, null, 2));

    const htmlBody: string = claudeRes.choices?.[0]?.message?.content ?? "<p>No digest generated.</p>";

    // 5. Send via Resend
    const emailRes = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${resendKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: "AI Digest <onboarding@resend.dev>",
        to: [RECIPIENT],
        subject: `AI Digest — ${today}`,
        html: `<!DOCTYPE html><html><body style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:24px;color:#1a1a1a;">${htmlBody}</body></html>`,
      }),
    }).then(r => r.json());

    console.log("Email sent:", emailRes.id ?? JSON.stringify(emailRes));

    return {
      date: today,
      hnStoriesFetched: hnAiItems.length,
      firecrawlResultsFetched: firecrawlArticles.length,
      totalArticles: allArticles.length,
      emailSent: true,
      emailId: emailRes.id,
    };
  },
});
