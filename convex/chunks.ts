import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: { moduleRef: v.id("modules") },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("chunks")
      .withIndex("by_module", (q) => q.eq("moduleRef", args.moduleRef))
      .collect();
  },
});

export const get = query({
  args: { id: v.id("chunks") },
  handler: async (ctx, args) => {
    return await ctx.db.get(args.id);
  },
});

const chunkFields = {
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
};

export const create = mutation({
  args: chunkFields,
  handler: async (ctx, args) => {
    return await ctx.db.insert("chunks", args);
  },
});

export const update = mutation({
  args: {
    id: v.id("chunks"),
    title: v.optional(v.string()),
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
  },
  handler: async (ctx, args) => {
    const { id, ...fields } = args;
    await ctx.db.patch(id, fields);
  },
});

export const remove = mutation({
  args: { id: v.id("chunks") },
  handler: async (ctx, args) => {
    // Cascade: delete all QA pairs for this chunk
    const qaPairs = await ctx.db
      .query("qaPairs")
      .withIndex("by_chunk", (q) => q.eq("chunkRef", args.id))
      .collect();
    for (const qa of qaPairs) {
      await ctx.db.delete(qa._id);
    }
    await ctx.db.delete(args.id);
  },
});
