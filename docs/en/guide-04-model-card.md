# Study Guide 04 — Reading Model Cards (Onboarding → 5-Paragraph Graduation)

> Companion to lecture 04.
> Assumes you have read [Guide 00](guide-00-foundations.md), [Guide 02 (vocabulary)](guide-02-vocabulary.md), and [Guide 03 (grammar)](guide-03-grammar.md).
> This guide brings everything together in real-material reading. Five paragraphs analyzed step-by-step.
> Read end-to-end (~60 min). Revisit each time you read a real model card.

---

## 0. Where You Are Now

You should have:
- **Guide 00 graduated**: intuition for Hanzi, radicals, pinyin, tones
- **220 vocabulary words**: 80%+ Anki hit rate
- **15 grammar patterns**: recognizable in real material

Built on top of that, this guide is full-paragraph reading. After reading this and analyzing the five paragraphs below, you should be able to handle a real model card alone. That is graduation.

---

## 1. The Universal Structure of Model Cards

Model cards are the **standard documentation format for ML models**. ModelScope, Hugging Face, ms-swift, FastChat — all use nearly the same structure.

Knowing this structure ahead of time is your first acceleration. **You can locate any specific piece of information instantly because you know what section it lives in.**

### The Five Standard Sections

Almost every model card has these five sections:

| # | Section | Standard Chinese header | Content |
|---|---------|------------------------|---------|
| 1 | Introduction | `模型简介` / `简介` / `模型介绍` | what / architecture / use cases |
| 2 | Specs | `模型规格` / `参数说明` / `模型参数` | parameters / context / quantization |
| 3 | Usage | `使用方法` / `快速开始` | Python code + environment |
| 4 | Benchmarks | `评测结果` / `性能` / `基准测试` | tables |
| 5 | License | `许可证` / `使用协议` / `License` | license + citation |

Some cards add `使用案例` (use cases), `已知限制` (limitations), `更新日志` (changelog), but the five above are nearly always present and they cover ~90% of locations you need.

### Reading Priority by Section

Your time is finite. Prioritize:

1. **Top priority — Introduction**: most-read section, formulaic patterns are clearest
2. **Specs**: numbers + Hanzi units, learns fast
3. **Benchmarks**: mostly tables, learn the header vocabulary
4. **Usage**: mostly English code, Hanzi only in inline notes
5. **License**: short and formulaic

Spend most of Month 2 on Introduction and Specs. Together they account for ~70% of model-card reading effort.

---

## 2. Section-by-Section Formulas — 90% Coverage if Internalized

Each section has near-fixed phrasings that show up across most model cards. Internalize these (more accurately: see them 5-10 times in real material) and your reading speed jumps.

### 2.1 Introduction Section Formulas

```
{model name} 是基于 {architecture} 的 {model type},支持 {capability 1}、{capability 2} 等任务。
该模型采用 {core technique} 设计,可用于 {use 1}、{use 2} 等场景。
```

**Translation**:
- "{model name} is a {model type} based on {architecture}, supporting {capability 1}, {capability 2}, and other tasks."
- "This model adopts {core technique} design, and can be used in {use 1}, {use 2}, and other scenarios."

**Real example**:
- `Qwen3 是基于 Transformer 的大语言模型,支持文本生成、推理、对话等任务。`
- `该模型采用 MoE 设计,可用于多种自然语言处理场景。`

These two sentences alone exercise three of the five core grammar patterns from Guide 03 (基于, 用于, 是...的). Reading one paragraph instantly validates that grammar learning.

### 2.2 Specs Section Formulas

```
总参数量为 {N} 亿
激活参数为 {M} 亿
支持上下文长度 {K}
最低显存要求 {V} GB
推荐显存 {W} GB
```

**Translation**:
- "Total parameter count is {N} 亿"
- "Activated parameters are {M} 亿" (MoE only)
- "Supports context length {K}"
- "Minimum VRAM requirement {V} GB"
- "Recommended VRAM {W} GB"

All formulaic. Only the variables change.

**Number unit reference**:
- `亿` = 100 million (NOT 100 billion!)
- `万` = 10,000
- `K` = 1,000 (千 also used)
- `B` = 1 billion (often left in English)

So `235亿` = 23.5B (235M is wrong!), `1万亿` = 1T. The Chinese unit `亿` confuses English speakers more than any other technical term — engrave the `亿 = 100M` mapping deeply.

### 2.3 Usage Section Formulas

```
首先,安装依赖:    (First, install dependencies)
然后,加载模型:    (Then, load the model)
最后,运行推理:    (Finally, run inference)
```

Or:

```
按照以下步骤使用:    (Use according to the following steps)
1. 安装 transformers
2. 下载模型权重
3. 加载模型
4. 运行推理
```

Code blocks are English. You only need to read Hanzi in inline notes. The most frequent Hanzi in this section:

```
首先 — first
然后 — then
最后 — finally
注意 — note / caution
确保 — ensure
推荐 — recommend
建议 — suggest
```

### 2.4 Benchmarks Section — Table Headers

The benchmarks section is mostly tables. Just learn the header vocabulary.

| Chinese header | Meaning |
|---------------|---------|
| 模型 / Model | model name |
| 评分 / Score | score |
| 准确率 | accuracy |
| 召回率 | recall |
| F1 / F1 分数 | F1 score |
| 吞吐量 | throughput |
| 时延 / 延迟 | latency |
| 速度 | speed |
| 对比 / 比较 | comparison |
| 提升 | improvement |
| 下降 | decrease |
| 平均 | average |

Frequently compared model names (in Chinese):

```
GPT-4 / Claude / Gemini  — usually English
通义千问 (Qwen)          — Chinese name
深度求索 (DeepSeek)      — Chinese name
智谱 / GLM (ChatGLM)     — Chinese name
零一万物 (01.AI / Yi)    — Chinese name
```

Some company names appear in Hanzi. Learn them once.

### 2.5 License Section Formulas

```
本模型采用 {license name} 协议发布。
商用 {允许/禁止/需要授权}。
学术使用 {允许}。
```

**Translation**:
- "This model is released under the {license} agreement"
- "Commercial use {permitted/forbidden/requires authorization}"
- "Academic use {permitted}"

Common license names:

```
Apache 2.0    — most common
MIT           — common
GPL / LGPL    — occasional
专属许可证 (proprietary license) — company-specific (caution)
```

Mastered in 5 minutes.

---

## 3. Five Practice Paragraphs — Step-by-Step Walkthroughs

Now we walk through five real-style model card paragraphs in detail. Each paragraph reflects a typical phrasing used by a major Chinese open-source LLM team.

For each paragraph:
1. Original
2. Word-by-word breakdown
3. Pattern identification
4. Combined translation
5. Learning notes

### 3.1 Qwen-style

**Original**:

```
Qwen3-235B-A22B 是基于 Transformer 架构的大语言模型,
支持文本生成、对话、推理等任务。
该模型采用 MoE 设计,总参数量为 2350 亿,激活参数为 220 亿,
可用于多种自然语言处理场景。
```

**Step 1 — Word breakdown**:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 是 | shì | is / to be |
| 基于 | jī yú | based on |
| 架构 | jià gòu | architecture |
| 的 | de | (modifier particle) |
| 大语言模型 | dà yǔ yán mó xíng | large language model (LLM) |
| 支持 | zhī chí | supports |
| 文本生成 | wén běn shēng chéng | text generation |
| 对话 | duì huà | dialogue |
| 推理 | tuī lǐ | inference |
| 等 | děng | etc. |
| 任务 | rèn wù | task |
| 该模型 | gāi mó xíng | this model |
| 采用 | cǎi yòng | adopts |
| 设计 | shè jì | design |
| 总参数量 | zǒng cān shù liàng | total parameter count |
| 为 | wéi | is |
| 亿 | yì | 100 million |
| 激活参数 | jī huó cān shù | activated parameters |
| 可用于 | kě yòng yú | can be used for |
| 多种 | duō zhǒng | various |
| 自然语言处理 | zì rán yǔ yán chǔ lǐ | natural language processing |
| 场景 | chǎng jǐng | scenario |

**Step 2 — Pattern identification**:

| Phrase | Pattern |
|--------|---------|
| `基于 Transformer 架构` | 3.4 (基于) |
| `支持...等任务` | 4.7 (支持) + 等 formula |
| `采用 MoE 设计` | basic V+O |
| `总参数量为 2350 亿` | specs formula |
| `可用于...场景` | 3.3 (用于) — 可+用于 |

**Step 3 — Combined translation**:

> Qwen3-235B-A22B is a large language model based on the Transformer architecture, supporting text generation, dialogue, inference, and other tasks. This model adopts MoE design, with a total parameter count of 235 billion and 22 billion activated parameters, and can be used in various natural language processing scenarios.

**Step 4 — Learning notes**:

- `2350 亿` = 235B (NOT 2.35T). The `亿` = 100M unit will trip you constantly until you have it engraved.
- `MoE` = Mixture of Experts, kept as English. Total vs. activated parameters is the MoE signature.
- `自然语言处理` = NLP. Translate as the English acronym in your notes.

---

### 3.2 DeepSeek-style

**Original**:

```
DeepSeek-R1 是一款专注于推理任务的大模型,
通过强化学习对模型进行对齐训练。
相比之前的版本,本次发布在数学推理和代码生成方面性能显著提升。
```

**Step 1 — Word breakdown**:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 一款 | yī kuǎn | a (kind of) (measure word) |
| 专注于 | zhuān zhù yú | focused on |
| 推理任务 | tuī lǐ rèn wù | reasoning tasks |
| 通过 | tōng guò | through |
| 强化学习 | qiáng huà xué xí | reinforcement learning (RL) |
| 对齐训练 | duì qí xùn liàn | alignment training |
| 相比 | xiāng bǐ | compared to |
| 之前的版本 | zhī qián de bǎn běn | previous version |
| 本次发布 | běn cì fā bù | this release |
| 在...方面 | zài...fāng miàn | in the aspect of |
| 数学推理 | shù xué tuī lǐ | mathematical reasoning |
| 代码生成 | dài mǎ shēng chéng | code generation |
| 性能 | xìng néng | performance |
| 显著提升 | xiǎn zhù tí shēng | significantly improved |

**Step 2 — Pattern identification**:

| Phrase | Pattern |
|--------|---------|
| `是一款...的` | 4.1 (是...的) — emphasis |
| `专注于...` | 用于 variant (specialized) |
| `通过 X 对 Y 进行 Z` | 4.5 (通过) + 3.5 (对...进行) compound |
| `相比之前的版本` | comparison expression |
| `在...方面` | scope expression |

**Step 3 — Combined translation**:

> DeepSeek-R1 is a large model focused on reasoning tasks, with alignment training performed on the model via reinforcement learning. Compared to previous versions, this release significantly improves performance in mathematical reasoning and code generation.

**Step 4 — Learning notes**:

- `一款` is a measure word for products, models, software. English just translates it as "a." Don't try to preserve it.
- `通过 X 对 Y 进行 Z` = compound structure "by doing X, perform Z on Y." This is the most frequent compound pattern in model cards. Memorize the shape.
- `显著` (significantly) appears constantly in benchmark comparisons. Pair it with `提升` (improvement) or `下降` (drop).

---

### 3.3 ChatGLM-style

**Original**:

```
若您的显存不足 16GB,建议使用 INT4 量化版本。
具体使用方法如下:首先安装 transformers,然后从 ModelScope 下载模型权重。
```

**Step 1 — Word breakdown**:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 若 | ruò | if (formal) |
| 您 | nín | you (formal) |
| 显存 | xiǎn cún | VRAM |
| 不足 | bù zú | insufficient |
| 建议 | jiàn yì | recommend |
| 使用 | shǐ yòng | use |
| 量化版本 | liàng huà bǎn běn | quantized version |
| 具体 | jù tǐ | specific / concrete |
| 使用方法 | shǐ yòng fāng fǎ | usage / how-to |
| 如下 | rú xià | as follows |
| 首先 | shǒu xiān | first |
| 安装 | ān zhuāng | install |
| 然后 | rán hòu | then |
| 从 | cóng | from |
| 下载 | xià zǎi | download |
| 模型权重 | mó xíng quán zhòng | model weights |

**Step 2 — Pattern identification**:

| Phrase | Pattern |
|--------|---------|
| `若...,建议...` | 4.4 (如果...就) variant — 若 + 建议 |
| `不足 16GB` | negation expression (insufficient + number) |
| `具体...如下` | usage-section formula |
| `首先...然后...` | sequence expression |

**Step 3 — Combined translation**:

> If your VRAM is less than 16GB, we recommend using the INT4 quantized version. The specific usage is as follows: first install transformers, then download the model weights from ModelScope.

**Step 4 — Learning notes**:

- `若` is the formal version of `如果`. More common in official documents and model cards.
- `您` is the polite form of `你`. Common in user-facing manuals.
- `首先...然后...最后...` is the standard sequence pattern in usage sections. Five encounters and it is automatic.

---

### 3.4 Yi-style

**Original**:

```
本模型在 200K 长上下文下表现稳定,
适用于文档分析、长文本摘要等场景。
注意:推理时显存占用较高,建议使用 80GB 以上的 GPU。
```

**Step 1 — Word breakdown**:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 本模型 | běn mó xíng | this model |
| 在 | zài | at / in |
| 长上下文 | cháng shàng xià wén | long context |
| 下 | xià | under |
| 表现 | biǎo xiàn | performs |
| 稳定 | wěn dìng | stable |
| 适用于 | shì yòng yú | applicable for |
| 文档分析 | wén dàng fēn xī | document analysis |
| 长文本摘要 | cháng wén běn zhāi yào | long-text summarization |
| 注意 | zhù yì | note / caution |
| 推理时 | tuī lǐ shí | during inference |
| 占用 | zhàn yòng | occupy |
| 较高 | jiào gāo | relatively high |
| 以上 | yǐ shàng | or above |

**Step 2 — Pattern identification**:

| Phrase | Pattern |
|--------|---------|
| `在...下` | condition expression (under) |
| `适用于...等场景` | 3.3 (用于) variant + 等 formula |
| `注意:` | caution header |
| `较高` | degree expression (-er) |
| `建议使用 80GB 以上的 GPU` | 4.6 (需要) variant — 建议 = recommended |

**Step 3 — Combined translation**:

> This model performs stably under 200K long context, applicable to scenarios such as document analysis and long-text summarization. Note: VRAM usage during inference is relatively high; we recommend using a GPU with 80GB or more.

**Step 4 — Learning notes**:

- `在 X 下` = "under X" — used for environment specification. English "under X conditions" or "given X."
- `较高 / 较低` = "relatively high/low." `较` = "comparatively."
- `200K` and similar quantities often stay in English. Mixed Hanzi-English is normal.

---

### 3.5 MiniMax-style

**Original**:

```
通过对模型进行 INT4 量化,显存占用减少 75%,推理速度提升约 2 倍。
量化后的模型在常见基准测试上的性能下降控制在 1% 以内。
```

**Step 1 — Word breakdown**:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 通过 | tōng guò | through |
| 对 | duì | on |
| 进行 | jìn xíng | perform |
| INT4 量化 | INT4 liàng huà | INT4 quantization |
| 减少 | jiǎn shǎo | decrease |
| 推理速度 | tuī lǐ sù dù | inference speed |
| 提升 | tí shēng | improve |
| 约 | yuē | approximately |
| 倍 | bèi | times (multiplier) |
| 量化后 | liàng huà hòu | post-quantization |
| 常见 | cháng jiàn | common / general |
| 基准测试 | jī zhǔn cè shì | benchmark test |
| 性能下降 | xìng néng xià jiàng | performance drop |
| 控制 | kòng zhì | control |
| 以内 | yǐ nèi | within |

**Step 2 — Pattern identification**:

| Phrase | Pattern |
|--------|---------|
| `通过对模型进行 INT4 量化` | 4.5 (通过) + 3.5 (对...进行) compound |
| `减少 75%, 提升约 2 倍` | numeric/degree expression |
| `量化后的模型` | post-action modifier (后的) |
| `在...上` | scope expression |
| `控制在 X 以内` | formula (kept within X) |

**Step 3 — Combined translation**:

> By performing INT4 quantization on the model, VRAM usage decreases by 75% and inference speed improves by approximately 2x. The quantized model's performance drop on common benchmarks is kept within 1%.

**Step 4 — Learning notes**:

- `通过对X进行Y` is the most frequent compound pattern in model cards. Memorize the shape, not just the components.
- `控制在 X 以内` ("kept within X") is a formula for performance bounds.
- `约` = approximately. Common in numeric estimates.

---

## 4. The Stuck-Point Workflow — 7 Steps

When you hit a wall in real material, here is the workflow.

```
You meet a sentence
    ↓
[Step 1] Identify domain vocabulary (in your 220?)
    ↓
[Step 2] Decompose remaining Hanzi into building blocks
    ↓
[Step 3] Identify grammar patterns (which of the 15?)
    ↓
[Step 4] Look up only the unknown words in Pleco
    ↓
[Step 5] Attempt full translation
    ↓
[Step 6] Compare with DeepL (weekly is enough)
    ↓
[Step 7] Note big divergences as learning points
```

### Each Step Detailed

**Step 1 — Domain vocabulary**

In any sentence, find words that belong to your 220-word set first. Usually 3-5 of 5-10 sentence words are domain vocabulary. Identifying these gives you the skeleton.

**Step 2 — Hanzi decomposition**

For words outside the 220 set, break each Hanzi into components. For English speakers, this is your main compounding tool — `具体` = `具` (concrete) + `体` (body) = "concrete." `实际上` = `实` (real) + `际` (boundary) + `上` (upon) = "in reality / actually."

**Step 3 — Pattern identification**

Look for the 15 grammar patterns. 把/将, 用于, 基于, 对...进行 — if you see these, half the parsing is done.

**Step 4 — Pleco lookup**

Now look up only the unknowns that remained. Usually 1-2 per sentence. No time waste.

**Step 5 — Full translation**

Translate to natural English. Don't preserve word order. Natural English is more accurate than literal.

**Step 6 — DeepL comparison (optional)**

Once a week, take one paragraph and compare with DeepL.

**Step 7 — Learning notes**

Big divergences are your learning points. Was it vocabulary? Grammar? Style? Add it to your weekly review.

### "You Don't Need Every Word" Principle

This rule from Guide 02 is most important here. Even if there are 5 unknowns in a sentence, getting 2-3 of them is usually enough for 80% comprehension. The other 2-3 you guess from context or skip.

**Wrong loop**: look up every unknown, add to Anki, can't move to next sentence.

**Correct loop**: 80% understanding → next sentence. After 5 encounters of the same word, you learn it.

---

## 5. The DeepL Comparison Method

DeepL is your verification tool, not the answer key. Especially useful early in learning.

### Weekly Workflow

```
1. Pick one model-card paragraph (50-100 chars)
2. Self-translate (time it)
3. Run DeepL
4. Compare side by side
5. Classify divergences:
   - Missed word → vocab gap
   - Grammar misread → revisit grammar.md
   - Literal vs. natural → ignore (DeepL is more natural but same meaning)
6. Note learning points
```

### Progress Curve

**Weeks 1-4**: DeepL crushes you. Self-translation misses 30-50% on average. Normal.

**Weeks 5-8**: closing in. Self-translation 80-90% accurate. DeepL still produces smoother English.

**Weeks 9-12**: occasional moments where your translation is more accurate than DeepL — especially when DeepL mistranslates a domain term.

**Weeks 13-16**: self-translation reliable. DeepL becomes a backup.

Measuring this curve directly fights motivation slumps.

---

## 6. Next Stops — Zhihu / CSDN

After your five model-card graduation, here is the difficulty ladder:

| Source | Difficulty | Character |
|--------|-----------|-----------|
| ModelScope cards | ★★ | Formulaic, ideal for learning |
| Hugging Face Chinese cards | ★★★ | Mixed Chinese/English |
| Zhihu troubleshooting | ★★★★ | Conversational + technical mix |
| CSDN posts | ★★★★ | Informal, deep domain |
| Juejin (掘金) writeups | ★★★ | Short and concrete |
| arXiv Chinese abstracts | ★★★★★ | Academic, post-graduation |

**Recommended order**: 5 model cards → 3 Zhihu answers → 2 CSDN posts → arXiv abstracts.

### What's Different About Each Source

**Zhihu**: blends conversational and technical registers. The mood particles you've been ignoring (吧, 啊) start showing up occasionally. About 80% of expressions still match model-card style.

**CSDN**: personal-blog tone. Informal but deep. More unfamiliar vocabulary than model cards. Highest learning value.

**Juejin**: short and practical. Lots of troubleshooting writeups. Difficulty between model cards and Zhihu.

**arXiv**: academic register, formal vocabulary (将, 若, 以...为, 即). Tackle after graduation.

---

## 7. Writing Your First GitHub Issue — Graduation Output 1

Graduation requires posting one real GitHub Issue.

### Standard Structure (see `templates/github-issue-template.md`)

```markdown
### 问题描述 (Problem)
{One-sentence summary}

### 复现步骤 (Reproduction)
1. 我使用 ...
2. 然后 ...
3. 出现以下错误:
\`\`\`
{error log}
\`\`\`

### 环境 (Environment)
- GPU: ...
- CUDA: ...
- PyTorch: ...
- 模型: ...

### 我尝试过的方法 (Attempted)
我尝试过 ...,但是 ...

### 期望行为 (Expected)
我希望 ...
```

One or two sentences per section is plenty. **Short and precise is good.** Error logs stay in English.

### Ten Common Phrases

```
我遇到了... — I have encountered ...
请问... — May I ask ...
如何... — How do I ...
是否支持... — Does it support ...
谢谢 — Thank you
请参考... — Please refer to ...
我已经尝试过... — I have already tried ...
但是没有解决 — But it did not resolve
期待您的回复 — Looking forward to your reply
非常感谢 — Thank you very much
```

These ten phrases handle nearly any GitHub Issue.

### Recommended Target OSS Projects

```
vLLM (PagedAttention inference engine)
ms-swift (Swift framework for LLMs)
FastChat (LLM serving)
ChatGLM (Zhipu's models)
Qwen (Alibaba's models)
DeepSeek-V3 (DeepSeek's models)
LLaMA-Factory (training framework)
```

Pick a project you actually use. Don't fabricate issues — collect real friction you have hit and write it up.

---

## 8. Graduation Checklist

Tick all eight to graduate:

- [ ] **Read Guide 00**
- [ ] **220 vocabulary words mastered in Anki** (80%+ hit rate)
- [ ] **15 grammar patterns auto-recognized**
- [ ] **5 model cards read in full** (each with the 5-step analysis)
- [ ] **3 Zhihu answers read**
- [ ] **2 CSDN posts read**
- [ ] **1 GitHub Issue posted** ✅ Graduation output 1
- [ ] **1 Zhihu answer posted (300+ chars)** ✅ Graduation output 2

All eight done = you have graduated the four-month curriculum.

---

## 9. After Graduation

Congratulations. You are not the same learner you were four months ago. Material that was unreadable on day one is now readable end-to-end. That is the result this curriculum committed to.

The next step is the daily reading habit and domain expansion. Keep reading one paragraph per day in Chinese forever. Expand into adjacent domains as your work demands.

This curriculum's four lectures end here. The material in your own field becomes your teacher from now on.

Thank you for staying through all four lectures.

—— MLOps Language Curriculum
