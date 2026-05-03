# 04 — Reading Our First ModelScope Model Card Together

> The fourth video script in this curriculum. Roughly 11 minutes.
> Watch this after lectures 02 and 03, once you have started memorizing the 220 words and have a working grasp of the 15 grammar patterns.

---

## Lecture Script

Hello. This is the fourth lecture. If you have been following along, you have started memorizing the 220 domain words and you now know what the 15 grammar patterns actually look like. But that is not the end of memorizing things. The real work starts now. So in this lecture, we are going to read an actual ModelScope model card together — one paragraph, one phrase at a time. Real practice.

Let me set up a scenario. You hear that Qwen3 has just been released, so you go to ModelScope. The URL looks something like `modelscope.cn/models/Qwen/Qwen3-235B-A22B`. You open the page, and the first paragraph reads roughly like this:

> Qwen3-235B-A22B 是基于 Transformer 架构的大语言模型,支持文本生成、对话、推理等任务。该模型采用 MoE 设计,总参数量为 2350 亿,激活参数为 220 亿,可用于多种自然语言处理场景。

When you see it for the first time, this looks intimidating. A solid wall of black characters. Let us walk through it slowly.

**First sentence, first half:** `Qwen3-235B-A22B 是基于 Transformer 架构的大语言模型`.

The model name `Qwen3-235B-A22B` is just a name, skip it. The next character is 是 — "is." Then 基于 — one of the 15 patterns from lecture 03. "Based on." Then `Transformer 架构`. The word 架构 is the building-block character pair "frame + structure" — you can read it directly as "architecture." (And the Korean and Japanese readers in the audience will recognize the cognate immediately.) Then 的 — the connective particle, roughly "of" or relative-clause "that." Then 大语言模型. Block by block: 大 = "big," 语言 = "language" (语 = "speech/language," 言 = "word"), 模型 = "model" (模 = "model/pattern," 型 = "type/form"). So the whole noun is "big-language-model" — which we read in English as "large language model," LLM.

Combine: **"Qwen3-235B-A22B is a large language model based on the Transformer architecture."** That flows.

**First sentence, second half:** `支持文本生成、对话、推理等任务`.

支持 — building blocks "support + hold." In context this just means "supports." Then 文本生成 — "text + generate" = "text generation." Then 对话 — "facing + speech" = "dialogue/conversation." Then 推理 — "push + reason" = "inference." Then 等 — "et cetera." Then 任务 — "duty + task" = "task."

Combine: **"...supports text generation, dialogue, inference, and other tasks."** Done. You have read the first sentence.

**Second sentence:** `该模型采用 MoE 设计,总参数量为 2350 亿,激活参数为 220 亿,可用于多种自然语言处理场景`.

该模型 — 该 means "this/that" in formal register, so 该模型 is "this model." 采用 — "pick + use" = "adopt." 设计 — "design + plan" = "design." So the first clause: **"This model adopts the MoE design."**

`总参数量为 2350 亿`. 总 — "total." 参数量 — "parameter quantity" = "parameter count." 为 — used here to mean "is/equals." 亿 — "100 million" (a single character that means "0.1 billion" in Chinese number conventions). So: **"Total parameter count is 235 billion."** Then `激活参数为 220 亿` — "activated parameters are 22 billion." That difference is the signature of MoE — only a slice of the model is activated per token.

`可用于多种自然语言处理场景`. 可用于 — "can be used for." 用于 is one of our 15 patterns. 多种 — "many + kinds" = "various." 自然语言处理 — "natural language processing," NLP. 场景 — "scene + setting" = "scenario/use case." Combine: **"It can be used for various natural language processing scenarios."**

Paragraph done. Combined translation:

> Qwen3-235B-A22B is a large language model based on the Transformer architecture, supporting text generation, dialogue, inference, and other tasks. The model adopts the MoE design, with a total parameter count of 235 billion and 22 billion activated parameters, and can be used for various natural language processing scenarios.

The block of black characters that intimidated you when you first saw it has just resolved into one clean sentence. It probably took you a while. That is normal. This is the first paragraph. The second and third paragraphs go faster, because the same expressions repeat.

Now let me give you a critical principle. **You do not need to know every word.** If 采用 was new to you in this paragraph, look it up once, jot down "adopt," move on. Do not try to memorize it. You will run into it in the next paragraph, and the next model card, and the one after that. After about five encounters, your brain memorizes it on its own — no flashcards required. This is the same "Don't memorize, encounter" rule from lecture 02.

So how do you verify when you get stuck? Paste the sentence into DeepL or ChatGPT and compare. Read it yourself first, then compare with the translation. The gaps are your learning points. At first the gaps will be wide. Around month one they shrink considerably. Around month two there are moments where your reading is more accurate than the machine translation. That is when first-language reading actually starts.

Congratulations on graduating from your first paragraph. Honestly, this is the most important milestone of the curriculum. The learners who have done this once and the learners who have not are categorically different. You are now in the first category.

The next steps are reading a full-page model card, then a Zhihu troubleshooting answer, then writing a GitHub Issue in Chinese yourself. All of this happens within 16 weeks. `docs/en/checklist.md` lays this out week by week — just follow it.

Thank you for sticking through these four lectures. These four are the orientation. The real learning starts when you read one paragraph of real material every day. One month from now, two months, four months — you will be reading material that the version of you watching this lecture cannot read. That is the result this curriculum commits to.

Thank you.

---

## Lecture Structure Notes

| Section | Approx. Time | Core Message |
|---------|--------------|--------------|
| Intro | 0:00 ~ 0:30 | Real practice begins |
| Scenario + opening paragraph | 0:30 ~ 1:30 | A representative Qwen3 card |
| First sentence (front) | 1:30 ~ 4:00 | 是 / 基于 / 大语言模型 |
| First sentence (back) | 4:00 ~ 5:30 | 支持 / 推理 / 任务 |
| Second sentence | 5:30 ~ 8:00 | 该 / 采用 / 用于 / 场景 |
| Combined translation + milestone | 8:00 ~ 9:00 | First-paragraph graduation |
| "Don't memorize, encounter" applied | 9:00 ~ 10:00 | Dictionary + DeepL verification flow |
| Next steps + sign-off | 10:00 ~ 11:00 | 16-week checklist pointer |

## Next Steps

- `docs/en/checklist.md` — 16-week weekly checklist
- `docs/en/grammar.md` — 15 grammar patterns with examples
- `docs/en/github-issue-template.md` — templates for writing issues in Chinese
