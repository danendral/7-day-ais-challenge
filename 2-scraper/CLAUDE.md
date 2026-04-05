# Day 2 — Web Scraper

Scrape, extract, crawl, map, and screenshot websites using the Firecrawl MCP server.

## What This Project Does
This is a web scraping toolkit powered by Firecrawl. It handles:
- **Scraping** single pages for content extraction (markdown, JSON, structured data)
- **Batch scraping** multiple URLs at once
- **Crawling** entire sites or sections with depth/page limits
- **Mapping** site structure and discovering all URLs
- **Searching** the web for relevant pages
- **Interacting** with dynamic pages (click, type, scroll)

## How It Works
All scraping is done via the **Firecrawl MCP server** connected to Claude Code. No local scraping scripts — just invoke the MCP tools directly.

See [firecrawl-cheatsheet.md](firecrawl-cheatsheet.md) for full tool reference and common workflows.

## Key Tools
| Tool | Use |
|------|-----|
| `firecrawl_scrape` | Single page extraction |
| `firecrawl_batch_scrape` | Multiple pages at once |
| `firecrawl_map` | Discover all URLs on a site |
| `firecrawl_crawl` | Crawl entire site/section |
| `firecrawl_search` | Web search |
| `firecrawl_agent` | Autonomous multi-source research |
| `firecrawl_interact` | Browser automation |

## Guidelines
- Always check the cheatsheet before using an unfamiliar tool
- Use `firecrawl_map` first when exploring unknown sites
- Set `maxPages` / `limit` to avoid burning API credits
- Use `onlyMainContent: true` to skip navbars/footers
- Store API key in `.env` (gitignored), never commit it
