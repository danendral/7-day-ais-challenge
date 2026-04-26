# 7 Day AIS Challenge

My journey through the [7 Day AIS Challenge](https://www.skool.com/ai-automation-society/classroom/dda699b7?md=2fc3ced36fc941f39b65fe63ae73b653) by [Nate Herk](https://www.youtube.com/@NateHerk) — building 7 AI automation projects in 7 days, from zero to a working portfolio.

## What is this?

A structured challenge from the [AI Automation Society](https://www.skool.com/ai-automation-society) where you build real AI automations using Claude Code, MCP servers, and deployment platforms like Trigger.dev. Each day introduces a new concept and a hands-on project.

## Daily Projects

| Day | Topic | Project | Status |
|-----|-------|---------|--------|
| 1 | The WAT Framework | Newsletter Automation | ✅ Done |
| 2 | MCP Servers | Web Scraping with Firecrawl | ✅ Done |
| 3 | Skills | Skill Builder & Reusable Skills | ✅ Done |
| 4 | Deployment | Daily AI Digest via Trigger.dev | ✅ Done |
| 5 | Website Building | Professional Landing Page | |
| 6 | Scheduled Automations | Self-Improving Scheduled Automation | |
| 7 | Executive Assistant | Capstone — Functional EA | |

## Day 1 — Newsletter Automation

Built an automated newsletter pipeline using the **WAT Framework** (Workflows, Agents, Tools):

- **Workflows** — Markdown SOPs that define objectives, inputs, tools, and edge cases
- **Agents** — AI handles orchestration and decision-making (not execution)
- **Tools** — Deterministic Python scripts for reliable execution (API calls, formatting, etc.)

The pipeline: research a topic via web search, generate an infographic, format as responsive HTML email, and send via Gmail.

**Key takeaway:** Separating AI reasoning from deterministic execution keeps accuracy high. If each step is 90% accurate, five chained steps drop to 59% — offloading execution to scripts solves this.

## Day 2 — Web Scraping with Firecrawl MCP

Learned how to connect external tools to Claude Code via **MCP (Model Context Protocol)** servers, using Firecrawl as the primary tool.

- Configured the Firecrawl MCP server in Claude Code settings
- Used `firecrawl_scrape` and `firecrawl_search` to extract structured data from websites
- Produced clean markdown output from scraped pages

**Key takeaway:** MCP servers extend Claude's capabilities with real-world tools (scraping, APIs, databases) without writing any integration code — just configure and use.

## Day 3 — Skills & Reusable Prompts

Explored Claude Code **Skills** — reusable slash commands that encode repeatable workflows into a single prompt file.

- Built and used custom skills for common tasks (PPT generation, code review, etc.)
- Learned how skills differ from memory: skills are actions, memory is context
- Applied the `ppt-builder` skill to generate a presentation from raw data

**Key takeaway:** Skills turn multi-step processes into one-line commands, making complex automations repeatable without re-explaining them each time.

## Day 4 — Daily AI Digest (Deployed to Trigger.dev)

Built and deployed a **scheduled automation** that runs every morning at 07:00 WIB (00:00 UTC) and emails a summarized AI news digest.

- Fetches top AI stories from **Hacker News** (filtered by 17 AI-related keywords)
- Searches for latest AI news via **Firecrawl** web search
- Summarizes everything using **Gemini 2.0 Flash** via OpenRouter
- Sends a formatted HTML email via **Resend**
- Deployed to Trigger.dev cloud — runs automatically, no local machine needed

**Stack:** TypeScript · Trigger.dev · OpenRouter (Gemini 2.0 Flash) · Firecrawl · Resend

## Tech Stack

- [Claude Code](https://claude.ai/claude-code) — AI coding & orchestration
- [Firecrawl](https://firecrawl.dev) — Web scraping via MCP
- [Trigger.dev](https://trigger.dev) — Deployment & scheduling platform
- [OpenRouter](https://openrouter.ai) — LLM API aggregator (cost-effective model access)
- [Resend](https://resend.com) — Transactional email

## Structure

Each day lives in its own folder:

```
1-newsletter-demo/
2-scraper/
3-claude-skill/
4-deploy-automation/
```

## Credits

Challenge created by [Nate Herk](https://www.youtube.com/@NateHerk) (AI Automation Society, Uppit AI).
