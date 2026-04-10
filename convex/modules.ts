import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  handler: async (ctx) => {
    return await ctx.db.query("modules").collect();
  },
});

export const get = query({
  args: { id: v.id("modules") },
  handler: async (ctx, args) => {
    return await ctx.db.get(args.id);
  },
});

export const create = mutation({
  args: {
    moduleId: v.string(),
    title: v.string(),
    description: v.string(),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("modules", args);
  },
});

export const update = mutation({
  args: {
    id: v.id("modules"),
    title: v.optional(v.string()),
    description: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    const { id, ...fields } = args;
    await ctx.db.patch(id, fields);
  },
});

export const remove = mutation({
  args: { id: v.id("modules") },
  handler: async (ctx, args) => {
    // Cascade: delete all chunks and their QA pairs
    const chunks = await ctx.db
      .query("chunks")
      .withIndex("by_module", (q) => q.eq("moduleRef", args.id))
      .collect();
    for (const chunk of chunks) {
      const qaPairs = await ctx.db
        .query("qaPairs")
        .withIndex("by_chunk", (q) => q.eq("chunkRef", chunk._id))
        .collect();
      for (const qa of qaPairs) {
        await ctx.db.delete(qa._id);
      }
      await ctx.db.delete(chunk._id);
    }
    await ctx.db.delete(args.id);
  },
});
