# Send Newsletter Workflow

## Objective
Take a topic from the user, research it, generate visual content, format as HTML email, and send to multiple recipients via Gmail.

## Required Inputs
- **Topic**: The subject to research and write about
- **Recipients**: Comma-separated email addresses (or a .txt/.csv file path)

## Required API Keys (in `.env`)
- `NANOBANANA_API_KEY` — from https://nanobananaapi.ai/api-key
- `OPENROUTER_API_KEY` (optional fallback) — from https://openrouter.ai/keys

## Pipeline Steps

### Step 1: Research the Topic (Agent-Driven)
- **Method**: Agent uses WebSearch to research the topic directly
- **Process**:
  1. Search for the topic using multiple queries
  2. Synthesize findings into structured JSON:
     ```json
     {
       "title": "Catchy newsletter title",
       "summary": "2-3 paragraph overview",
       "key_points": ["point 1", "point 2", ...],
       "stats": ["stat 1", "stat 2", ...],
       "sources": ["url1", "url2", ...]
     }
     ```
  3. Save to `.tmp/newsletter_data.json`
- **Fallback**: If agent research isn't available, run `tools/research_topic.py` which uses OpenRouter (perplexity/sonar-pro). Requires `OPENROUTER_API_KEY` in `.env`.

### Step 2: Generate Infographic
- **Tool**: `tools/generate_infographic.py`
- **Input**: Visual description derived from research key points
- **Output**: PNG image saved to `.tmp/`, base64 string for embedding
- **Edge cases**: 
  - API is async — tool polls every 5s for up to 5 minutes
  - If generation fails, continue without infographic (text-only newsletter)
  - Image URLs expire after 10 minutes, so the tool downloads immediately

### Step 3: Format as HTML Email
- **Tool**: `tools/format_newsletter.py`
- **Input**: Research data + optional infographic base64
- **Output**: Responsive HTML email at `.tmp/newsletter.html`
- **Note**: Uses inline CSS for email client compatibility. Infographic is base64-embedded.

### Step 4: Send via Gmail
- **Method**: Gmail MCP tool (built into Claude Code)
- **Pre-requisite**: Authenticate Gmail MCP if not already done
- **Process**: 
  1. Read the HTML from `.tmp/newsletter.html`
  2. Send to each recipient with the newsletter title as subject
  3. Confirm delivery for each recipient

## Running the Pipeline

### Primary flow (agent-driven research):
1. Agent researches topic via WebSearch
2. Agent saves research JSON to `.tmp/newsletter_data.json`
3. Run: `python tools/run_newsletter.py --research-file .tmp/newsletter_data.json "email1,email2"`
4. Agent sends via Gmail MCP

### Fallback flow (fully automated):
```bash
python tools/run_newsletter.py "Your Topic" "email1@example.com,email2@example.com"
```
Requires `OPENROUTER_API_KEY` in `.env`.

## Quick Agent Checklist
1. Confirm topic and recipients with user
2. Research topic using WebSearch
3. Save structured research to `.tmp/newsletter_data.json`
4. Run `tools/run_newsletter.py --research-file ...` for infographic + HTML
5. Review the HTML output (open `.tmp/newsletter.html`)
6. Authenticate Gmail MCP if needed
7. Send the email to all recipients
8. Confirm success to user

## Known Constraints
- Nano Banana API requires a callback URL (we pass a dummy and poll instead)
- Nano Banana `type` field has a typo in their API: use `"TEXTTOIAMGE"` not `"TEXTTOIMAGE"`
- Large infographic base64 can increase email size significantly — monitor for email size limits (~25MB for Gmail)
