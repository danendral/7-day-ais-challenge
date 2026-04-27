# Day 6 — Schedule and Loop

Automate recurring tasks using Claude Code's scheduling system and loop capabilities.

## What This Project Explores
- **Scheduling** — running Claude agents on a cron schedule (e.g. every morning)
- **Looping** — iterating over data sources (inbox threads, git repos, files)
- **MCP tool access in scheduled agents** — Gmail, git, file system

## Use Cases Built

### 1. Morning Coffee Status — Gmail Digest
A scheduled agent that scans Gmail for recent unread threads, summarizes each in one line (sender + topic + urgency), and writes the output to `morning-coffee-status.md`.

- **MCP used:** `mcp__claude_ai_Gmail__search_threads`, `mcp__claude_ai_Gmail__get_thread`
- **Schedule:** Daily at a configured time
- **Output:** `morning-coffee-status.md`

### 2. Daily Git Progress Logger
A scheduled agent that reads a list of project repos from `~/.claude/my-projects.json`, runs `git log` across all of them, summarizes commits with AI, adds a random AI inspirational quote, and appends a daily entry to `progress.md`.

- **Config:** `~/.claude/my-projects.json` — list of repo paths to scan
- **Schedule:** Every morning
- **Output:** Appends to `progress.md` (running log across all projects)
- **Ran via:** Claude desktop app (cowork session)

## Key Concepts

| Concept | Description |
|---------|-------------|
| `schedule` skill | Creates recurring Claude Code routines on a cron schedule |
| `loop` skill | Runs a prompt repeatedly at a set interval |
| Scheduled agent | A Claude agent that runs autonomously in the background |
| `my-projects.json` | Config file listing repo paths for cross-project git scanning |

## How Scheduling Works in Claude Code
- Scheduled agents are configured via the `schedule` skill in Claude Code CLI
- They do NOT run in the Claude desktop app — the desktop app is conversational only
- The output (markdown files) can be read from the desktop app after the fact
- Agents run in a specified working directory with access to configured MCP tools

## Limitations Discovered
- Claude desktop app cannot run background scheduled tasks natively
- Gmail MCP connects to a specific authenticated account — verify which account is linked
- Scheduled agents need explicit repo paths; they don't auto-discover projects

## Files
| File | Purpose |
|------|---------|
| `morning-coffee-status.md` | Output of Gmail digest agent |
| `CLAUDE.md` | This file — day 6 documentation |
