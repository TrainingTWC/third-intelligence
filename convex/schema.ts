import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  modules: defineTable({
    moduleId: v.string(),
    title: v.string(),
    description: v.string(),
  }).index("by_moduleId", ["moduleId"]),

  chunks: defineTable({
    moduleRef: v.id("modules"),
    chunkId: v.string(),
    title: v.string(),
    intent: v.optional(v.string()),
    content: v.optional(v.string()),
    tags: v.optional(v.array(v.string())),
    context: v.optional(v.array(v.string())),
    priority: v.optional(v.number()),
    weight: v.optional(v.number()),
    responseTemplates: v.optional(v.array(v.string())),
    steps: v.optional(v.array(v.string())),
    failurePatterns: v.optional(v.array(v.string())),
    coachingActions: v.optional(v.array(v.string())),
    metricsImpacted: v.optional(v.array(v.string())),
    examplesGood: v.optional(v.array(v.string())),
    examplesBad: v.optional(v.array(v.string())),
    conditions: v.optional(v.array(v.string())),
    triggerSignals: v.optional(v.array(v.string())),
    rules: v.optional(v.array(v.string())),
    source: v.optional(v.string()),
    roleRelevanceBarista: v.optional(v.string()),
    roleRelevanceShiftManager: v.optional(v.string()),
    roleRelevanceStoreManager: v.optional(v.string()),
  }).index("by_module", ["moduleRef"]),

  qaPairs: defineTable({
    chunkRef: v.id("chunks"),
    instruction: v.string(),
    output: v.string(),
  }).index("by_chunk", ["chunkRef"]),
});
