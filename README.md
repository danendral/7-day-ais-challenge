# 7 Day AIS Challenge

My journey through the [7 Day AIS Challenge](https://www.skool.com/ai-automation-society/classroom/dda699b7?md=2fc3ced36fc941f39b65fe63ae73b653) by [Nate Herk](https://www.youtube.com/@NateHerk) — building 7 AI automation projects in 7 days, from zero to a working portfolio.

## What is this?

A structured challenge from the [AI Automation Society](https://www.skool.com/ai-automation-society) where you build real AI automations using Claude Code, MCP servers, and deployment platforms like Trigger.dev. Each day introduces a new concept and a hands-on project.

## Daily Projects

| Day | Topic | Project | Status |
|-----|-------|---------|--------|
| 1 | The WAT Framework | Newsletter Automation | Done |
| 2 | MCP Servers | Web Scraping with Firecrawl | |
| 3 | Skills | Skill Builder & Reusable Skills | |
| 4 | Deployment | Deploy Automation to Trigger.dev | |
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

## Tech Stack

- [Claude Code](https://claude.ai/claude-code) — AI coding & orchestration
- [Firecrawl](https://firecrawl.dev) — Web scraping via MCP
- [Trigger.dev](https://trigger.dev) — Deployment platform
- [n8n](https://n8n.io) — Workflow automation

## Structure

Each day lives in its own folder:

```
1-newsletter-demo/
2-.../
3-.../
...
```

## Credits

Challenge created by [Nate Herk](https://www.youtube.com/@NateHerk) (AI Automation Society, Uppit AI).
