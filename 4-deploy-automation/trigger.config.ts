import { defineConfig } from "@trigger.dev/sdk/v3";

export default defineConfig({
  project: "proj_ilcsizekyeiimvtkhzua",
  dirs: ["src/trigger"],
  maxDuration: 300, // 5 minutes — enough for HN fetch + Firecrawl + LLM + email
});
