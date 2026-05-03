# Study Guide 03 — Grammar Mastery (Onboarding → 15-Pattern Graduation)

> Companion to lecture 03.
> Assumes you have read [Guide 00 (zero-stage)](guide-00-foundations.md) and [Guide 02 (vocabulary)](guide-02-vocabulary.md).
> This guide is the detailed manual for: how do sentences actually parse? Why is 15 grammar patterns enough?
> Read end-to-end (~60 min). Revisit each pattern after every 5 encounters in real material.

---

## 0. How to Read This Guide

The flow:

1. **Why 15 patterns is enough** — the core argument. If you don't accept this, you will lose motivation halfway.
2. **Mandarin word order basics** — short section. Most of it is good news.
3. **The five core patterns** — deeply, with 5-7 examples each, variations, and traps.
4. **The ten additional patterns** — quickly, but enough to recognize them in real material.
5. **Practical analysis** of one paragraph showing all patterns in action.
6. **Self-diagnostic** at Week 4 to verify you can identify patterns automatically.

Nothing to memorize from this guide directly. Read for understanding, then let real-material exposure automate recognition.

---

## 1. Speaking Grammar vs. Reading Grammar — Different Skill Sets

Let me start with a strange fact.

Most non-native English speakers I work with cannot fluently hold a conversation in English. But they read English READMEs daily without much trouble. Same person, two very different proficiency levels.

How does this happen?

Answer: **conversational grammar and reading grammar are largely separate skill domains**. The overlap is smaller than people assume.

Conversational English needs: everyday expressions, question inversions, rhythm and pronunciation, idiomatic phrasings. Reading English needs: sentence skeletons (SVO + modifiers), formulaic technical phrases ("it is X that...", "given that...", "provided that..."), domain vocabulary, and contextual inference. Both are English, but the items you learn are different. You can be strong in one and weak in the other.

### Mandarin Has the Same Split

The most important grammar group in spoken Mandarin is the family of **mood particles (语气助词)**. They have no clean equivalent in English. The four main ones:

```
吧 (ba) — soft suggestion / urging
   你来吧 → "come on, come over"

啊 (a) — emphasis / exclamation
   你来啊 → "come on, come!"

呢 (ne) — questioning / contrast
   你来呢? → "what about you, are you coming?"

嘛 (ma) — obviousness / mild complaint
   你来嘛 → "just come, will you"
```

These look almost identical but carry subtle different tones. Mastering them is the heart of conversational Mandarin and the hardest thing for foreign speakers.

**Now — do mood particles appear in ModelScope model cards?**

Almost never. Technical documentation is not transmitting a speaker's emotion or social register. It is transmitting facts. Mood particles, by definition, encode emotion. So they do not appear in technical writing — model cards, papers, READMEs, GitHub Issues, Zhihu answers all have nearly zero usage of 吧 啊 呢 嘛.

**This means**: the most central skill in conversational Chinese has zero priority in our curriculum. You can ignore it entirely.

### What Reading Grammar Actually Needs

The structures that actually appear in technical Chinese:

```
把 / 将 — disposal construction ("dispose of X by doing Y")
用于 — "is used for"
基于 — "based on"
对...进行 — "perform Y on X"
```

These five cover roughly half of what you will encounter in any model card. They almost never appear in conversation (too formal, too stilted), so conversation-first courses introduce them late or not at all. We introduce them in Week 1.

**Add five more**: 是...的 (emphasis), 不/没 (negation), 可以/能 (capability), 如果...就 (conditional), 通过 (through).

**And five more**: 需要 (need), 支持 (support), 被 (passive), serial verbs, 得 (degree complement). Total: 15.

These 15 cover 80%+ of model cards and READMEs. Four weeks of focused learning. That is the whole grammar phase.

---

## 2. Mandarin Word Order — Mostly Good News

### Good News: SVO

Mandarin is **Subject-Verb-Object**. Same as English.

```
我      训练    模型
I       train   the model
```

If you are coming from English, **just use your English instinct**. Form the sentence in English structure, then swap in Hanzi. It works.

This is a major advantage compared to Korean or Japanese learners, who come from SOV languages and have to fight an instinct to put the verb at the end.

### No Verb Conjugation

You learned this in Guide 00, but it is worth repeating because it is the most counterintuitive thing for new learners. Mandarin verbs do not change form.

| Meaning | Mandarin |
|---------|----------|
| I train | 我训练 |
| I trained | 我训练**了** |
| I have trained | 我训练**过** |
| I am training | 我**在**训练 |
| I will train | 我**将**训练 |

`训练` never changes. Helper words (`了 / 过 / 在 / 将`) do the tense work.

### Modifier Placement

Adjective before noun: `大模型` (large model). Same as English (large model).

Time/location at front: `今天我训练模型` (today I train the model). Time-fronting is more common than in English but not weird.

Modifier + 的 + head noun: `开源的模型` (open-source model, lit. "open-source's model"). Functions like English relative clauses.

---

## 3. The Five Core Patterns — Half of Every Model Card

These five patterns appear, on average, **5-10 times per model card paragraph**. Auto-recognizing them unlocks half of any model card.

For each: definition → 5-7 examples → variations → traps.

---

### 3.1 把 (bǎ) — Disposal Construction

**Meaning**: "Dispose of X by doing Y to it."

In English, this often translates as "convert X to Y," "load X into Y," "save X as Y." The structure highlights *what was processed and how*.

**Structure**:

```
Subject + 把 + Object + Verb + Complement (where to / what into / how)
```

**Seven examples**:

1. `把模型转换为 ONNX 格式` — Convert the model to ONNX format
2. `把数据加载到内存` — Load the data into memory
3. `把权重保存到 checkpoint` — Save weights to a checkpoint
4. `把模型部署到 GPU` — Deploy the model to GPU
5. `把输入序列截断为 512` — Truncate the input sequence to 512
6. `把损失函数定义为交叉熵` — Define the loss function as cross-entropy
7. `把这些层冻结` — Freeze these layers

**Why this pattern shows up so often**

Technical documentation needs to express "what was done to what." 把 makes the manipulated object explicit and grammatically prominent. It is more precise than the simple SVO `我训练模型` for cases where the result of the manipulation matters.

**Critical trap — the verb cannot stand alone**

In a 把 disposal sentence, the verb must be followed by a **complement**. The complement is the "into / to / as / completely" piece.

```
✗ 把模型训练       — incomplete; no complement
✓ 把模型训练完了    — Finished training the model (complement: 完了 "completed")
✓ 把模型训练成最佳状态 — Trained the model into optimal state (complement: 成最佳状态)
```

If you see 把 without a complement attached to the verb, it is either ungrammatical or you are missing context.

---

### 3.2 将 (jiāng) — Formal Equivalent of 把

**Meaning**: Same as 把, but more formal.

In technical documents, papers, and official communications, 将 is far more common than 把. Casual READMEs and blogs lean toward 把. About 90% of model cards use 将.

**Structure**: Same as 把.

```
Subject + 将 + Object + Verb + Complement
```

**Five examples**:

1. `将参数初始化为 0` — Initialize the parameters to 0
2. `将模型量化至 INT4` — Quantize the model to INT4
3. `本节将介绍核心算法` — This section will introduce the core algorithm
4. `将权重转换为 fp16` — Convert weights to fp16
5. `将训练时间缩短到 3 天` — Shorten training time to 3 days

**Rule of thumb**: model cards / papers → 将. Casual READMEs → 把. Recognize both.

### 将's Other Use — Future Tense

将 also functions as a future-tense marker, separately from its disposal construction usage.

```
将发布 v3 版本 — will release v3 version
将支持长上下文 — will support long context
```

Here 将 is roughly English "will" or "shall." When 将 appears immediately before a verb (no object preceding), it is a future marker. When it appears in the disposal construction (Subject + 将 + Object + Verb + Complement), it is the formal version of 把.

---

### 3.3 用于 (yòng yú) — "Is Used For"

**Meaning**: A is used for B / A is intended for B

**Structure**:

```
Subject + 用于 + purpose
```

**Seven examples**:

1. `该模型用于文本生成` — This model is used for text generation
2. `该框架用于推理加速` — This framework is used for inference acceleration
3. `本工具用于调试` — This tool is used for debugging
4. `适用于多种场景` — Applicable to various scenarios (适用于 variant)
5. `可用于工业部署` — Can be used for industrial deployment (可用于 variant)
6. `专用于科学计算` — Dedicated to scientific computing (专用于 variant)
7. `主要用于研究` — Mainly used for research

**Why this appears in the first sentence of every README**

A model card needs to answer "what is this model for?" early. 用于 (or its variants) is the standard expression for that. It appears in roughly the first two sentences of 99% of model cards.

**Priority**: memorize first. Learn this in Week 1.

---

### 3.4 基于 (jī yú) — "Based On"

**Meaning**: B based on A / A as the foundation of B

**Structures**:

```
基于 + A + 的 + B    (B based on A — noun phrase)
基于 + A + Verb       (verb something based on A)
```

**Seven examples**:

1. `基于 Transformer 架构` — based on the Transformer architecture
2. `基于 LoRA 微调` — based on LoRA fine-tuning
3. `基于注意力机制的模型` — model based on the attention mechanism
4. `基于强化学习的对齐` — alignment based on reinforcement learning
5. `基于 PyTorch 实现` — implemented based on PyTorch
6. `基于 fp8 的训练方案` — fp8-based training scheme
7. `本系统基于 Kubernetes 构建` — This system is built on Kubernetes

**Why this is a fixed expression in model introductions**

Every new model has to answer "what architecture / approach is it built on?" 基于 is the standard answer. It appears in the third sentence of nearly every model card.

**Priority**: memorize second.

---

### 3.5 对...进行 (duì...jìnxíng) — "Perform Y on X"

**Meaning**: Perform B on A / Apply B to A

In English: "perform Y on X," "apply Y to X."

**Structure**:

```
对 + A + 进行 + B
   (on A)   (perform B)
```

**Seven examples**:

1. `对模型进行量化` — Quantize the model
2. `对参数进行初始化` — Initialize the parameters
3. `对数据进行预处理` — Preprocess the data
4. `对结果进行评估` — Evaluate the results
5. `对损失进行优化` — Optimize the loss
6. `对模型进行 INT8 量化` — Apply INT8 quantization to the model
7. `对长序列进行截断` — Truncate long sequences

**Why this is genuinely high-frequency**

In technical Chinese, when you say "perform an operation on an object," `对X进行Y` is the natural construction. Both `量化模型` and `对模型进行量化` mean "quantize the model," but the second is more formal and more common in model cards.

**Routine appearance: 5-10 times per model card.** Treat it as a fixed expression.

**Translation note**: in English, you usually do not say "perform quantization on the model" — you say "quantize the model." Don't try to preserve the structure. Translate to natural English: `对X进行Y` → "Y the X" or "perform Y on X" depending on flow.

---

## 4. Ten Additional Patterns — to 80% Coverage

The five core patterns cover 50%. These ten add another 30%.

### 4.1 是...的 (shì...de) — Emphasis

**Meaning**: It is X that... / X is the one that...

```
该模型是基于 Transformer 的 — This model **is** Transformer-based
该方法是有效的 — This method is effective (with emphasis)
```

In technical writing, used for "this is the key characteristic" emphasis.

### 4.2 不 / 没 (bù / méi) — Negation

| Negator | Use |
|---------|-----|
| 不 | future / habitual / state | 不支持 (does not support) |
| 没 | past / completion | 没训练 (has not been trained) |

不 dominates in technical writing. 没 mostly for "has not yet" expressions.

```
不支持 fp8 — does not support fp8
不需要预训练 — does not require pre-training
没经过对齐 — has not undergone alignment
```

### 4.3 可以 / 能 (kěyǐ / néng) — Capability

**Both translate as "can." The distinction is subtle.**

- `可以` — permission / general possibility
- `能` — ability / capacity

```
可以使用 INT4 — can use INT4 (possibility)
能加载 70B 模型 — can load a 70B model (capacity)
```

Both common in technical text. Don't overthink the distinction.

### 4.4 如果...就 / 那么 (rúguǒ...jiù) — Conditional

**Meaning**: If X, then Y

```
如果显存不够,就使用量化 — If VRAM is insufficient, use quantization
如果是 fp8,那么需要 H100 — If fp8, then H100 is required
若不支持 fp8,使用 fp16 — If fp8 is not supported, use fp16
```

`若` is the formal version of `如果`, common in more formal documents.

### 4.5 通过 (tōngguò) — "Through / By Means Of"

**Meaning**: Via A, do B / By means of A

```
通过 LoRA 微调 — through LoRA fine-tuning
通过 API 调用 — through API calls
通过对模型进行量化,显存减少 75% — by performing quantization on the model, VRAM is reduced by 75%
```

Frequently combined with `对...进行` — `通过对X进行Y` is a compound structure you will see often.

### 4.6 需要 (xūyào) — "Need / Require"

```
需要 80GB 显存 — requires 80GB VRAM
需要 PyTorch 2.0 以上 — requires PyTorch 2.0 or above
需要 GPU 支持 — requires GPU support
```

Standard for the requirements section.

### 4.7 支持 (zhīchí) — "Support"

```
支持 INT4 量化 — supports INT4 quantization
不支持流式输出 — does not support streaming output
仅支持英文 — supports English only
```

Standard for feature lists. Almost always in the first paragraph.

### 4.8 被 (bèi) — Passive

```
模型被部署到 GPU — The model is deployed to GPU
参数被初始化为 0 — Parameters are initialized to 0
该方法被广泛采用 — This method is widely adopted
```

Less frequent in Chinese technical writing than English passive. When it appears, there is often a slight emphasis effect.

### 4.9 Serial Verb Construction (V1 + V2)

Two verbs in sequence, where V1 expresses the means/purpose of V2.

```
使用 Python 训练模型 — Train the model using Python
下载模型部署到本地 — Download and deploy the model locally
打开终端运行命令 — Open the terminal and run the command
```

English "use X to do Y" or "do X and Y." Very common in usage sections.

### 4.10 得 (de) — Degree Complement

```
性能提升得很快 — Performance improves very quickly
训练得不充分 — Training is insufficient
读得很流畅 — Reads very smoothly
```

Roughly "X-ly" adverbs in English, or "so X that..." constructions. Common in performance comparisons.

---

## 5. Practical Application — Analyzing One Paragraph

Now let us see all 15 patterns in action on a real-style paragraph.

**Source**:

```
该模型基于 Transformer 架构,采用 MoE 设计,可用于多种推理场景。
通过对模型进行 INT4 量化,显存占用减少 75%。
支持长上下文,需要至少 80GB 显存。
```

**Pattern identification**:

| Phrase | Pattern | Interpretation |
|--------|---------|----------------|
| `基于 Transformer 架构` | 3.4 (基于) | "based on Transformer architecture" |
| `采用 MoE 设计` | basic V+O | "adopts MoE design" |
| `可用于多种推理场景` | 3.3 variant (用于) | 可 + 用于 = "can be used for" |
| `通过对模型进行 INT4 量化` | 4.5 + 3.5 (通过 + 对...进行) | "by performing INT4 quantization on the model" |
| `显存占用减少 75%` | basic V+O+complement | "VRAM usage decreases by 75%" |
| `支持长上下文` | 4.7 (支持) | "supports long context" |
| `需要至少 80GB 显存` | 4.6 (需要) | "requires at least 80GB VRAM" |

**Combined translation**:

> This model is based on Transformer architecture, adopts MoE design, and can be used in various inference scenarios. By performing INT4 quantization on the model, VRAM usage is reduced by 75%. It supports long context and requires at least 80GB of VRAM.

**Seven grammar patterns in one paragraph**, five of them in your core 15. Once you can identify these automatically, model-card reading speed jumps significantly.

---

## 6. Word-Order Exposure Training

Grammar is **absorbed by exposure, not memorized**. Read one model-card paragraph daily and actively identify the 15 patterns.

### Daily Workflow

```
[1] Pick one model-card paragraph (50-100 chars)
[2] Split into sentences
[3] Mark which of the 15 patterns appear in each
[4] Attempt full translation
[5] Compare with DeepL (weekly is enough)
```

### Recognition Targets

| Week | Auto-recognition rate |
|------|------------------------|
| 4 | 20% |
| 8 | 60% |
| 12 | 90% |
| 16 | Subconscious |

### Recommended Reading Variety

Read different model cards each day. Repeating the same one creates over-fitting on its phrasing. Suggested rotation:

- Weeks 1-2: Qwen series (2-3 cards)
- Weeks 3-4: DeepSeek series (2-3 cards)
- Weeks 5-6: ChatGLM, Yi series (2 each)
- Weeks 7-8: Domain-specific (autonomous driving / multimodal / speech / your area)

---

## 7. Self-Diagnostic (End of Week 4)

Identify the patterns in these five sentences:

1. `将权重量化至 4 比特` → which pattern?
   <details><summary>Answer</summary>3.2 将 (formal disposal). "Quantize the weights to 4 bits."</details>

2. `用于多模态任务` → which pattern?
   <details><summary>Answer</summary>3.3 用于. "Used for multimodal tasks."</details>

3. `基于 RLHF 进行对齐训练` → which two patterns?
   <details><summary>Answer</summary>3.4 基于 + 3.5 对...进行 variant. "Perform alignment training based on RLHF."</details>

4. `如果不支持 fp8,就使用 fp16` → which two patterns?
   <details><summary>Answer</summary>4.4 如果...就 + 4.7 支持. "If fp8 is not supported, use fp16."</details>

5. `该方法被广泛采用` → which pattern?
   <details><summary>Answer</summary>4.8 被 (passive). "This method is widely adopted."</details>

If you can identify 4 of 5, you have cleared the Month 1 grammar bar.

---

## 8. Slump Management + What's Next

The grammar slump usually hits Week 6-7. You memorize 15 patterns, but real material throws variations at you and they look unfamiliar.

This is usually a **vocabulary problem disguised as a grammar problem**. The patterns are intact; the words inside them are unknown, so the sentence does not parse. Diagnostic question: when you see a difficult sentence, is the structure unclear, or are most words unknown?

If most words unknown → revisit Guide 02 (vocabulary).
If structure unclear despite known words → re-read this guide and add 5 more example sentences per pattern.

### Next Study Guide

- [04 — Reading Model Cards (in practice)](guide-04-model-card.md)

Combining the 15 patterns with the 220 vocabulary, Guide 04 walks through five model-card paragraphs in detail. You will see grammar + vocabulary fuse into actual reading.

### Reference

- [grammar.md — 15 patterns + 4 bonus, with extended examples](grammar.md)

If you want more example sentences per pattern, that file has 5-10 additional examples each.

The path to 15-pattern mastery is now clear. Thanks.
