# Firecrawl MCP Server Cheatsheet

Quick reference for all Firecrawl MCP tools available in Claude Code.

---

## Tools Overview

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `firecrawl_scrape` | Extract content from a single URL | You know the exact page |
| `firecrawl_batch_scrape` | Scrape multiple URLs at once | You have a list of pages |
| `firecrawl_map` | Discover all URLs on a site | You need to find pages first |
| `firecrawl_crawl` | Crawl an entire site or section | You want to analyze a whole site |
| `firecrawl_search` | Web search | You don't know the source URL |
| `firecrawl_agent` | Autonomous multi-source research | Complex research tasks |
| `firecrawl_interact` | Browser automation (click, type, etc.) | Dynamic/interactive content |

---

## Tool Details

### 1. `firecrawl_scrape`
Extracts content from a single URL in multiple formats.

**Parameters:**
- `url` (string, required) — the webpage to scrape
- `formats` (array) — output formats: `markdown`, `json`, `branding`
- `onlyMainContent` (boolean) — skip navbars/footers, extract main content only
- `jsonSchema` (object) — define a structured schema for JSON extraction

**Example use case:** Scrape a blog post, product page, or documentation page.

---

### 2. `firecrawl_batch_scrape`
Scrapes multiple URLs simultaneously with built-in rate limiting.

**Parameters:**
- `urls` (array, required) — list of URLs to scrape
- `formats` (array) — output formats
- `jsonSchema` (object) — structured extraction schema

**Example use case:** Scrape 10 product pages at once to compare specs.

---

### 3. `firecrawl_map`
Discovers all URLs and sitemaps on a website.

**Parameters:**
- `url` (string, required) — starting domain
- `includeSubdomains` (boolean) — whether to include subdomains
- `limit` (number) — max URLs to discover

**Example use case:** Before crawling, map the site to understand its structure and pick which pages to scrape.

---

### 4. `firecrawl_crawl`
Crawls multiple pages starting from a URL with configurable depth/limits.

**Parameters:**
- `url` (string, required) — starting page
- `maxPages` (number) — maximum pages to crawl
- `formats` (array) — output formats
- `limit` (number) — result constraints

**Example use case:** Crawl an entire documentation site or blog section.

---

### 5. `firecrawl_search`
Performs web search to find relevant pages.

**Parameters:**
- `query` (string, required) — search terms
- `limit` (number) — max number of results

**Example use case:** Find articles about a topic when you don't have a specific URL.

---

### 6. `firecrawl_agent`
Autonomous research agent that navigates across multiple sources.

**Parameters:**
- `objective` (string, required) — the research goal
- `tools` (array) — capabilities to use
- `maxSteps` (number) — operation limit

**Example use case:** "Find the pricing and features of the top 3 competitors in X space."

---

### 7. `firecrawl_interact`
Browser automation for interacting with dynamic page elements.

**Parameters:**
- `action` (string) — action type: `click`, `type`, `navigate`, `scroll`, etc.
- `selector` (string) — CSS selector for target element
- `value` (string) — input data for type actions

**Example use case:** Fill out a form, click through pagination, interact with SPAs.

---

## Common Workflows

### Scrape a known page
```
firecrawl_scrape → url: "https://example.com/page", formats: ["markdown"]
```

### Explore then scrape a site
```
firecrawl_map → url: "https://example.com"     (discover pages)
firecrawl_batch_scrape → urls: [picked URLs]    (scrape the ones you need)
```

### Research a topic
```
firecrawl_search → query: "topic keywords"      (find relevant pages)
firecrawl_scrape → url: best result              (get full content)
```

### Full site analysis
```
firecrawl_crawl → url: "https://example.com", maxPages: 50
```

---

## Configuration (already set up in `.env`)
- `FIRECRAWL_API_KEY` — required for authentication
- Retry max attempts default: 3
- Credit warning threshold default: 1000
