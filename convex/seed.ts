import { mutation } from "./_generated/server";
import { v } from "convex/values";

/** Insert a full module with nested chunks and QA pairs in one transaction. */
export const insertModule = mutation({
  args: {
    moduleId: v.string(),
    title: v.string(),
    description: v.string(),
    chunks: v.array(
      v.object({
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
        qaPairs: v.array(
          v.object({
            instruction: v.string(),
            output: v.string(),
          })
        ),
      })
    ),
  },
  handler: async (ctx, args) => {
    const moduleRef = await ctx.db.insert("modules", {
      moduleId: args.moduleId,
      title: args.title,
      description: args.description,
    });

    for (const chunk of args.chunks) {
      const { qaPairs, ...chunkData } = chunk;
      const chunkRef = await ctx.db.insert("chunks", {
        moduleRef,
        ...chunkData,
      });
      for (const qa of qaPairs) {
        await ctx.db.insert("qaPairs", {
          chunkRef,
          instruction: qa.instruction,
          output: qa.output,
        });
      }
    }
  },
});

/** Delete all data from all three tables. */
export const clearAll = mutation({
  handler: async (ctx) => {
    const qaPairs = await ctx.db.query("qaPairs").collect();
    for (const qa of qaPairs) await ctx.db.delete(qa._id);

    const chunks = await ctx.db.query("chunks").collect();
    for (const chunk of chunks) await ctx.db.delete(chunk._id);

    const modules = await ctx.db.query("modules").collect();
    for (const mod of modules) await ctx.db.delete(mod._id);

    return { deleted: { qaPairs: qaPairs.length, chunks: chunks.length, modules: modules.length } };
  },
});
