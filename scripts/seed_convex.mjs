/**
 * Seed Convex database from data/data.json
 *
 * Usage:
 *   node scripts/seed_convex.mjs
 *
 * Reads CONVEX_URL from .env.local (created by `npx convex dev`).
 */

import { readFileSync } from "fs";

// Read Convex URL from .env.local or environment
let CONVEX_URL = process.env.CONVEX_URL;
if (!CONVEX_URL) {
  try {
    const envFile = readFileSync(".env.local", "utf-8");
    const match = envFile.match(/CONVEX_URL=(.+)/);
    if (match) CONVEX_URL = match[1].trim();
  } catch { /* ignore */ }
}
if (!CONVEX_URL) {
  console.error("CONVEX_URL not found. Run `npx convex dev` first or set CONVEX_URL env var.");
  process.exit(1);
}
console.log(`Convex URL: ${CONVEX_URL}\n`);

async function callMutation(path, args = {}) {
  const res = await fetch(`${CONVEX_URL}/api/mutation`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ path, args, format: "json" }),
  });
  const data = await res.json();
  if (data.status !== "success") {
    throw new Error(`Mutation ${path} failed: ${JSON.stringify(data)}`);
  }
  return data.value;
}

// Load data.json
const raw = readFileSync("data/data.json", "utf-8");
const data = JSON.parse(raw);
console.log(`Loaded ${data.modules.length} modules from data/data.json\n`);

// Clear existing data
console.log("Clearing existing data...");
const deleted = await callMutation("seed:clearAll");
console.log("  Deleted:", deleted);

// Insert modules one by one
let totalChunks = 0;
let totalQA = 0;

for (const mod of data.modules) {
  const chunks = (mod.chunks || []).map((c) => ({
    chunkId: c.chunk_id || "",
    title: c.title || "",
    intent: c.intent || undefined,
    content: c.content || undefined,
    tags: c.tags || undefined,
    context: c.context || undefined,
    priority: c.priority || undefined,
    weight: c.weight || undefined,
    responseTemplates: c.response_templates || undefined,
    steps: c.steps || undefined,
    failurePatterns: c.failure_patterns || undefined,
    coachingActions: c.coaching_actions || undefined,
    metricsImpacted: c.metrics_impacted || undefined,
    examplesGood: c.examples?.good || undefined,
    examplesBad: c.examples?.bad || undefined,
    conditions: c.conditions || undefined,
    triggerSignals: c.trigger_signals || undefined,
    rules: c.rules || undefined,
    source: c.source || undefined,
    roleRelevanceBarista: c.role_relevance?.barista || undefined,
    roleRelevanceShiftManager: c.role_relevance?.shift_manager || undefined,
    roleRelevanceStoreManager: c.role_relevance?.store_manager || undefined,
    qaPairs: (c.qa_pairs || []).map((q) => ({
      instruction: q.instruction,
      output: q.output,
    })),
  }));

  const qaCount = chunks.reduce((sum, c) => sum + c.qaPairs.length, 0);
  totalChunks += chunks.length;
  totalQA += qaCount;

  await callMutation("seed:insertModule", {
    moduleId: mod.id,
    title: mod.title,
    description: mod.description || "",
    chunks,
  });

  console.log(`  ✓ ${mod.title} — ${chunks.length} chunks, ${qaCount} QA pairs`);
}

console.log(`\n═══ DONE ═══`);
console.log(`  ${data.modules.length} modules, ${totalChunks} chunks, ${totalQA} QA pairs seeded`);
