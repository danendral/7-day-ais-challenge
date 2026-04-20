---
name: ppt-builder
description: Use when someone asks to generate a ppt from data, put data into a presentation, create a powerpoint for management, or build slides from numbers/charts.
argument-hint: [file path or data]
---

Generates a professional, concise PPTX presentation from data for management audiences. Blue color scheme, 16:9 widescreen, 2-8 slides max.

## Process

1. **Read the input** — Read the file at `$ARGUMENTS` if a path is given, or use pasted/raw data. Support CSV, Excel, JSON, PDF, plain text. If the format is unreadable, stop and tell the user.
2. **Analyze the data** — Extract key metrics, percentages, increases/decreases, trends, and outliers. Identify what matters most to a management audience.
3. **Plan the slide structure** — Group data into logical topics. Decide how many slides (2-8). Each slide should have a single clear focus. Do NOT add filler or introductory fluff — go straight to the data.
4. **Write the spec JSON** — Build a JSON spec following the format below. This is the single source of truth that drives PPT generation.
5. **Generate the PPTX** — Run the bundled script:
   ```
   python .claude/skills/ppt-builder/scripts/generate_pptx.py <spec_path> output/<filename>.pptx
   ```
   Use a descriptive filename based on the presentation topic (e.g., `output/q3-revenue-summary.pptx`).
6. **Validate** — Re-read the input data and compare every number in the spec against the source. If any number is wrong, fix the spec and regenerate. Do NOT skip this step.
7. **Final review** — Open the generated file metadata. Confirm: correct slide count, no blank slides, charts rendered, metrics visible, no fabricated data.

## Slide Types

Use these types in the spec JSON:

- **title** — First slide. Presentation name, optional subtitle and date.
- **content** — Key metrics with optional bullet points. Use `metrics` for KPI cards (with deltas for increases/decreases), `bullets` for commentary, `right_notes` for secondary info.
- **chart** — Charts only or charts + notes. Up to 4 charts per slide (2x2 grid for multiple, full-width for single).
- **summary** — Key takeaways + next steps. Dark background for visual closure.

## Spec JSON Format

```json
{
  "slides": [
    {
      "type": "title",
      "title": "Presentation Title",
      "subtitle": "Optional subtitle",
      "date": "Optional date"
    },
    {
      "type": "content",
      "title": "Slide Title",
      "metrics": [
        {
          "label": "Revenue",
          "value": "$1.2M",
          "delta": { "direction": "up", "value": "+12% YoY" }
        }
      ],
      "bullets": ["Key insight 1", "Key insight 2"],
      "right_notes": "Optional context"
    },
    {
      "type": "chart",
      "title": "Slide Title",
      "charts": [
        {
          "type": "bar",
          "title": "Chart Title",
          "categories": ["Q1", "Q2", "Q3"],
          "series": [
            { "name": "Revenue", "values": [100, 200, 300] }
          ]
        }
      ],
      "notes": "Optional footnote"
    },
    {
      "type": "summary",
      "title": "Key Takeaways",
      "takeaways": ["Takeaway 1", "Takeaway 2"],
      "next_steps": ["Action 1", "Action 2"]
    }
  ]
}
```

## Chart Types

Use the simplest chart that fits the data:
- `bar` — Column chart. Default for comparisons.
- `stacked_bar` — Stacked column. For part-to-whole with multiple series.
- `bar_horizontal` — Horizontal bars. For long category names.
- `line` — Line chart. For trends over time.
- `pie` — Pie chart. Max 5-6 slices. Only for simple proportions.

## Rules

- **2-8 slides max.** If data requires more, prioritize what matters most. Never exceed 8.
- **Never fabricate data.** Only use numbers from the input. If a calculation is needed, show your work.
- **Deltas matter.** Always highlight increases (▲) and decreases (▼) when comparing periods or targets.
- **Simple visuals only.** No 3D charts, no overloaded pies, no decorative elements. Data is the focus.
- **Management tone.** Concise, actionable, no jargon. Every bullet should earn its place.
- **Validate after generation.** Compare every number in the spec against source data before delivering.

## Notes

- The script handles all formatting: blue theme, 16:9, metric cards, chart styling, slide backgrounds.
- Write the spec JSON to a temp file (e.g., `output/_spec.json`) before running the script.
- If python-pptx is not installed, run `pip install python-pptx` first.
- For very large datasets, summarize before building slides — don't try to show every row.
