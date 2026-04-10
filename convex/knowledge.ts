import { query } from "./_generated/server";

/**
 * Returns the full knowledge base in the same nested format as data.json
 * so the RAG engine can consume it directly.
 */
export const getAll = query({
  handler: async (ctx) => {
    const modules = await ctx.db.query("modules").collect();
    const result = [];

    for (const mod of modules) {
      const chunks = await ctx.db
        .query("chunks")
        .withIndex("by_module", (q) => q.eq("moduleRef", mod._id))
        .collect();

      const chunksWithQA = [];
      for (const chunk of chunks) {
        const qaPairs = await ctx.db
          .query("qaPairs")
          .withIndex("by_chunk", (q) => q.eq("chunkRef", chunk._id))
          .collect();

        chunksWithQA.push({
          chunk_id: chunk.chunkId,
          title: chunk.title,
          intent: chunk.intent,
          content: chunk.content,
          tags: chunk.tags,
          context: chunk.context,
          priority: chunk.priority,
          weight: chunk.weight,
          response_templates: chunk.responseTemplates,
          steps: chunk.steps,
          failure_patterns: chunk.failurePatterns,
          coaching_actions: chunk.coachingActions,
          metrics_impacted: chunk.metricsImpacted,
          examples:
            chunk.examplesGood || chunk.examplesBad
              ? { good: chunk.examplesGood, bad: chunk.examplesBad }
              : undefined,
          conditions: chunk.conditions,
          trigger_signals: chunk.triggerSignals,
          rules: chunk.rules,
          source: chunk.source,
          role_relevance:
            chunk.roleRelevanceBarista || chunk.roleRelevanceShiftManager || chunk.roleRelevanceStoreManager
              ? { barista: chunk.roleRelevanceBarista, shift_manager: chunk.roleRelevanceShiftManager, store_manager: chunk.roleRelevanceStoreManager }
              : undefined,
          qa_pairs: qaPairs.map((q) => ({
            instruction: q.instruction,
            output: q.output,
          })),
        });
      }

      result.push({
        id: mod.moduleId,
        title: mod.title,
        description: mod.description,
        chunks: chunksWithQA,
      });
    }

    return { modules: result };
  },
});
