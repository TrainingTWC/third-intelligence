import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: { chunkRef: v.id("chunks") },
  handler: async (ctx, args) => {
    return await ctx.db
      .query("qaPairs")
      .withIndex("by_chunk", (q) => q.eq("chunkRef", args.chunkRef))
      .collect();
  },
});

export const create = mutation({
  args: {
    chunkRef: v.id("chunks"),
    instruction: v.string(),
    output: v.string(),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("qaPairs", args);
  },
});

export const update = mutation({
  args: {
    id: v.id("qaPairs"),
    instruction: v.optional(v.string()),
    output: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { id, ...fields } = args;
    await ctx.db.patch(id, fields);
  },
});

export const remove = mutation({
  args: { id: v.id("qaPairs") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
  },
});
