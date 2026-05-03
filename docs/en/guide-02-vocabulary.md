# Study Guide 02 — Vocabulary Mastery (Onboarding → 220-Word Graduation)

> Companion to lecture 02.
> This guide assumes you have read [Guide 00 (the zero-stage)](guide-00-foundations.md). Hanzi, radicals, pinyin, and tones are explained in detail there.
> This guide builds on that foundation and walks through vocabulary acquisition: why we start with domain words, how Hanzi compounding works for English speakers, the actual 220-word breakdown, Anki workflow, and the "encounter, don't memorize" principle.
> Read once end-to-end (~45 min), then revisit weekly during your Month 1 vocabulary push.

---

## 0. How to Read This Guide

Two kinds of content alternate throughout:

**Concepts** — "Why domain words first," "How Hanzi compounding works." Read once, understand, move on. Don't memorize.

**Actions** — Anki setup, daily routine, handling new words in real material. These you apply every day.

Best path: read all concepts cover-to-cover first, then start acting on the action items the following day.

---

## 1. Why You Start with Domain Vocabulary — The Frequency Trick

If you walked into a generic Chinese class today, the first vocabulary you would meet is 你好 (nǐ hǎo, "hello"), 我 (wǒ, "I"), 谢谢 (xiè xie, "thank you"). The next chapter would cover 吃饭 (chī fàn, "eat"), 学校 (xué xiào, "school"), 朋友 (péng you, "friend").

This is the **standard sequence for conversational Chinese**, and if your goal is conversation, it is correct.

But pause for a second. Your goal is reading model cards on ModelScope and finding vLLM OOM solutions on Zhihu. Will any of those words show up there?

**Almost none of them.**

I ran a small experiment. I took the first 1,000 characters of a Qwen3 model card on ModelScope and counted how many words overlap with HSK levels.

```
HSK 1 (150 words)              → 25 appear in the model card
HSK 2 (300 cumulative)         → 50
HSK 3 (600 cumulative)         → 80
HSK 4 (1,200 cumulative)       → 120

Domain words in the model card not in any HSK level:
                               → 200+
```

So memorizing all of HSK 1 covers about 12% of a model card. Even working all the way through HSK 4 — 1,200 words — gets you to 60-70%. The remaining 30-40% is technical domain vocabulary that no general curriculum teaches.

### The Frequency Asymmetry

A core insight you need to internalize: **words in any language are not evenly distributed.** A handful of words appear extremely often; most words rarely appear at all. This skewed distribution is called Zipf's law in linguistics, and it shapes how much you need to learn to function in a domain.

For everyday Chinese, the threshold is around 1,500-2,000 words for ~80% comprehension of conversational material.

**For MLOps Chinese, the distribution is even more compressed.** Around 200-300 words give you ~80% comprehension of any model card. Why? Because domain vocabulary repeats relentlessly. 模型, 训练, 推理, 部署, 量化 — these five words appear in every single model card, often multiple times per page.

**This compression is what makes the curriculum possible.** 220 carefully chosen domain words give you the same coverage that a generic learner needs a full year to reach. Korean speakers can hit graduation in 4 months. English speakers need 6-8 months because Hanzi acquisition is slower without cognate intuition. Either way, the time savings versus a conventional path are enormous.

### Why Not Just Layer This On Top of HSK?

Some people ask: can I take HSK classes in parallel? The answer is — you can, but you will be paying double tuition for half the rate.

HSK classes are speaking-and-listening heavy. An hour of conversation drill produces maybe 20% of the reading progress that an hour of model-card reading produces. We deliberately cut speaking and listening for this reason. **If your goal is reading, optimize for reading.** Speaking is a separate 6-12 month investment you can add after you graduate.

---

## 2. Hanzi Strategy — How to Actually Memorize

So we have established: domain words first, 220 of them. The next question is: do we memorize at the word level or the Hanzi level?

The answer up front: **memorize at the word level, and Hanzi will come along for free.** Here is why.

### Hanzi Are Building Blocks

Recall from Guide 00: each Hanzi carries meaning. Hanzi compose to form multi-character words, and the meaning of the components shows through. Once you internalize one Hanzi, you unlock dozens of words.

Consider 推 ("push, derive"). You learned in Guide 00 that the radical is 扌 (hand) and the character carries the nuance of "pushing with hand." That single piece of knowledge unlocks:

```
推理 (push + reason)        = inference
推论 (push + theory)        = deduction
推断 (push + judge)         = inference, in another sense
推荐 (push + recommend)     = recommendation
推动 (push + move)          = drive forward, propel
```

Five words, all illuminated by one Hanzi. In an ML context, 推理 is "model inference," 推荐 is "recommender system," 推动 is "drive a project forward." The shared meaning of 推 is visible in all of them.

Another example. 量 ("measure, quantity"):

```
量化 (measure + transform)  = quantization
增量 (increase + measure)   = increment
考量 (examine + measure)    = consideration
测量 (test + measure)       = measurement
```

And 集 ("gather"):

```
集群 (gather + group)       = cluster
数据集 (data + gather)      = dataset
集成 (gather + form)        = integration
集中 (gather + center)      = concentrate
```

**This is the Hanzi multiplier.** One Hanzi = one building block. 100 Hanzi = ~1,000 multi-character words. This is what makes Hanzi qualitatively different from learning Latin alphabet roots — Hanzi *are* the meaning, not just hints toward meaning.

### What English Speakers Have Instead of Cognates

If you are Korean or Japanese, your native vocabulary already shares a huge stock of Hanzi-derived words with Chinese. You see 部署 and your brain immediately maps it to a familiar word in your language meaning "department" or "deployment." That is a free year of vocabulary.

You as an English speaker do not have this. **What you have is systematic decomposition.**

For each Hanzi you learn, you also learn its English meaning gloss. Then that gloss compounds across every word the Hanzi appears in. Over 500 Hanzi, you have built a system that decodes thousands of multi-character technical words by composition. The Korean learner gets there via cognate recognition. You get there via decomposition. Same destination, different paths.

The downside: decomposition is slower than recognition for the first few weeks. The upside: once you have ~300 Hanzi, the compounding rate is astonishing — each new Hanzi unlocks 5-10 new words you can read by composition.

### So Which Hanzi Do You Memorize First?

Answer: **memorize the 220 domain words, and the ~500 component Hanzi will be learned automatically as a byproduct.**

Don't go buy a "1,500 Hanzi" book and try to memorize them in isolation. That is inefficient. Memorize words. The Hanzi inside those words will repeat across the vocabulary set, and you will absorb them through repetition.

For example, the Hanzi 模 appears in:
- 模型 (model)
- 模板 (template)
- 模式 (pattern, mode)
- 规模 (scale)

Memorizing those four words means you have seen 模 four times in different contexts. By the fourth encounter, you know what it means without ever having "studied" it directly. **Words are the unit of learning. Hanzi are the byproduct.**

---

## 3. The 220 Domain Words by Category

Master file: `vocab/mlops-domain-vocab.csv`. Five categories.

### Category 1: Models & Architecture (70+ words)

**What this covers**: vocabulary describing models themselves — what kind of model, what architecture, what training method.

**Why it's the largest**: about half of any model card is descriptive of the model itself, so the vocabulary clusters here.

**Five core Hanzi**:

```
模 (mó)    — pattern, model
型 (xíng)  — form, type
训 (xùn)   — instruct
练 (liàn)  — practice
推 (tuī)   — push, derive
```

Words built from those five Hanzi alone:

| Word | Pinyin | Meaning |
|------|--------|---------|
| 模型 | mó xíng | model |
| 模板 | mó bǎn | template |
| 模式 | mó shì | pattern, mode |
| 规模 | guī mó | scale |
| 类型 | lèi xíng | type |
| 训练 | xùn liàn | training |
| 训练集 | xùn liàn jí | training set |
| 预训练 | yù xùn liàn | pre-training |
| 微调 | wēi tiáo | fine-tuning |
| 推理 | tuī lǐ | inference |
| 推断 | tuī duàn | inference (alt. sense) |

**Five Hanzi → eleven words.** Each Hanzi appears in 2-3 of the words on average. Learn the Hanzi once, watch it compound.

Other essential vocabulary in this category:

```
架构 (jià gòu)        — architecture
参数 (cān shù)        — parameter
神经网络 (shén jīng wǎng luò) — neural network
注意力 (zhù yì lì)    — attention
机制 (jī zhì)         — mechanism
权重 (quán zhòng)     — weight
偏置 (piān zhì)       — bias
梯度 (tī dù)          — gradient
损失 (sǔn shī)        — loss
优化 (yōu huà)        — optimization
学习率 (xué xí lǜ)    — learning rate
正则化 (zhèng zé huà) — regularization
批量 (pī liàng)       — batch
轮次 (lún cì)         — epoch
迭代 (dié dài)        — iteration
对齐 (duì qí)         — alignment
蒸馏 (zhēng liú)      — distillation
检索 (jiǎn suǒ)       — retrieval (the R in RAG)
增强 (zēng qiáng)     — augmented
```

These are unfamiliar at first, but each character carries clear meaning. 学习率: 学 (learn) + 习 (practice) + 率 (rate) = "learning rate," exactly what you would guess.

### Category 2: Infrastructure & Deployment (50+ words)

**What this covers**: how the model is deployed, served, scaled. Containers, clusters, GPU memory, quantization.

**Five core Hanzi**:

```
部 (bù)    — section, place
署 (shǔ)   — arrange, place
容 (róng)  — contain
器 (qì)    — instrument, container
量 (liàng) — measure, amount
```

**Key vocabulary**:

```
部署 (bù shǔ)         — deployment
容器 (róng qì)        — container
镜像 (jìng xiàng)     — image (Docker)
集群 (jí qún)         — cluster
显存 (xiǎn cún)       — VRAM
显卡 (xiǎn kǎ)        — graphics card
量化 (liàng huà)      — quantization
压缩 (yā suō)         — compression
推理引擎 (tuī lǐ yǐn qíng) — inference engine
推理框架 (tuī lǐ kuàng jià) — inference framework
分布式 (fēn bù shì)   — distributed
节点 (jié diǎn)       — node
分片 (fēn piàn)       — shard
副本 (fù běn)         — replica
负载 (fù zài)         — load
均衡 (jūn héng)       — balance (e.g., load balancer)
```

English acronyms (GPU, CPU, RAM) are commonly mixed into Chinese tech writing. You will routinely see `GPU 显存` (GPU VRAM) or `CPU 推理` (CPU inference) — fully mixed expressions. This is normal and you do not need to translate the English parts.

### Category 3: Performance & Evaluation (20+ words)

**What this covers**: performance measurement language. Throughput, latency, accuracy.

**Why so few words**: small category, but extremely high frequency. These all appear in the benchmarks section of nearly every model card.

**Key vocabulary**:

```
吞吐量 (tūn tǔ liàng) — throughput (lit. "swallow-spit-quantity")
时延 (shí yán)        — latency
延迟 (yán chí)        — latency (alternative term)
算力 (suàn lì)        — compute power
评测 (píng cè)        — benchmark / evaluation
评估 (píng gū)        — evaluation
基准 (jī zhǔn)        — baseline / benchmark
准确率 (zhǔn què lǜ)  — accuracy
召回率 (zhào huí lǜ)  — recall
精确率 (jīng què lǜ)  — precision
错误率 (cuò wù lǜ)    — error rate
速度 (sù dù)          — speed
性能 (xìng néng)      — performance
对比 (duì bǐ)         — comparison
```

吞吐量 is a delightful word — literally "swallow-spit-amount." That visual makes throughput easy to remember.

### Category 4: Data & Pipeline (25+ words)

**What this covers**: dataset, preprocessing, tokenization.

**Key vocabulary**:

```
数据集 (shù jù jí)    — dataset
样本 (yàng běn)       — sample
标注 (biāo zhù)       — annotation / labeling
标签 (biāo qiān)      — label / tag
预处理 (yù chǔ lǐ)    — preprocessing
分词 (fēn cí)         — tokenization
词表 (cí biǎo)        — vocabulary
词汇 (cí huì)         — vocabulary (alt.)
编码 (biān mǎ)        — encoding
解码 (jiě mǎ)         — decoding
管道 (guǎn dào)       — pipeline
流水线 (liú shuǐ xiàn) — pipeline (alt., literally "flowing-water-line")
清洗 (qīng xǐ)        — cleaning
增广 (zēng guǎng)     — augmentation
切分 (qiē fēn)        — split
划分 (huà fēn)        — divide
```

管道 and 流水线 both mean pipeline and you will see both depending on the author. Learn both.

### Category 5: General (50+ words)

**What this covers**: not domain-specific, but high-frequency in any technical writing. Verbs, connectors, framing words.

**Six core Hanzi**:

```
支 (zhī)   — support
持 (chí)   — hold
基 (jī)    — foundation
于 (yú)    — at, in
用 (yòng)  — use
通 (tōng)  — through
```

**Key vocabulary**:

```
支持 (zhī chí)        — supports
不支持 (bù zhī chí)   — does not support
采用 (cǎi yòng)       — adopts
基于 (jī yú)          — based on
通过 (tōng guò)       — through
适用 (shì yòng)       — applicable
适用于 (shì yòng yú)  — applicable for
用于 (yòng yú)        — used for
可用 (kě yòng)        — available
需要 (xū yào)         — needs / requires
要求 (yāo qiú)        — requires
依赖 (yī lài)         — depends on
实现 (shí xiàn)       — implements
提供 (tí gōng)        — provides
包括 (bāo kuò)        — includes
包含 (bāo hán)        — contains
```

These are tightly linked to the 15 grammar patterns covered in Guide 03. 用于, 基于, 通过 are simultaneously vocabulary items and grammatical structures. Learning vocabulary in this category automatically advances your grammar learning.

### Priority Order If You Are Time-Constrained

If you cannot do all 220 words within Month 1, prioritize this way:

1. **Tier 1 (50 words)**: All of Category 5 (general verbs and connectors). Without these, sentence structure does not parse.
2. **Tier 2 (70 words)**: All of Category 1 (models and architecture).
3. **Tier 3 (50 words)**: Category 2 (infrastructure and deployment).
4. **Tier 4 (20 words)**: Category 3 (performance and evaluation).
5. **Tier 5 (25 words)**: Category 4 (data and pipeline).

Try to do all 220 if possible. It is one month of work.

---

## 4. Anki Setup — Step by Step

Time to set up your spaced-repetition tool. We use **Anki**, free and battle-tested.

### Step 1: Generate the Vocabulary CSV

From the repository root:

```bash
python3 scripts/build_vocab.py
```

This populates `vocab/build/` with language-specific CSV files:

```
vocab/build/vocab-ko.csv  ← For Korean speakers
vocab/build/vocab-en.csv  ← For English speakers (you)
vocab/build/vocab-zh.csv  ← Pinyin only (reference)
```

### Step 2: Install Anki

Download from [apps.ankiweb.net](https://apps.ankiweb.net/). Free for Windows / macOS / Linux. Free for Android (AnkiDroid). $25 one-time for iOS (AnkiMobile). The mobile app is worth paying for if you have any commute or downtime — 10 minutes per day on phone is a major learning multiplier.

### Step 3: Import the CSV

1. Open Anki desktop
2. Create a new deck — name it "MLOps Chinese"
3. File → Import → select `vocab/build/vocab-en.csv`
4. Field mapping:
   - Front field: `front` (Hanzi)
   - Back field: `back` (English + pinyin)
5. Note type: Basic
6. Confirm import — you should see 220 cards

### Step 4: Set Daily Pace

| Pace | New cards/day | Days to clear new |
|------|---------------|-------------------|
| Standard (4 mo) | 30 | ~8 days for English speakers (target 50/day actually) |
| Accelerated (3 mo) | 50 | ~5 days |
| Slow (5-6 mo) | 15 | ~15 days |

For an English-speaking learner, I recommend **starting at 30/day for the first week** to get a feel for the algorithm, then bumping to 50/day. English speakers need more total Hanzi exposure than Korean speakers, and the way to get it is faster cycling.

Reviews per day: leave at unlimited. Anki will queue what needs review.

### Step 5: Daily Routine

```
Morning or commute:
  10 min — Anki new + reviews

Evening:
  25 min — read one paragraph of a real model card
  10 min — log unknown words + add edge cases to Anki
```

Same time each day if you can. The spaced-repetition algorithm assumes a stable cadence.

### Step 6: Handling Hard Cards

Some cards will refuse to stick. After 5+ failures on the same card:

1. Press "Suspend" in Anki to take it out of rotation
2. Note it in a personal stuck list
3. Encounter it organically in real material 3-4 more times
4. Unsuspend after it shows up in your reading

This protects your daily session from being dominated by 5% of the cards. Most cards (80%) follow the normal SRS curve. The stubborn 20% finish via real-material exposure.

---

## 5. Hanzi Decomposition — Your Compounding Tool

This section is where English speakers do their leverage work. Korean speakers get this leverage from Sino-Korean cognates; you get it from systematic decomposition.

### The Core Move

For every word you memorize, also note the meanings of its component Hanzi. Then watch the meanings compound across the rest of the vocabulary.

Example workflow:

```
Word: 量化
Component 1: 量 = "measure, quantity"
Component 2: 化 = "transform, -ize"
Composed meaning: "make quantitative" = quantization
```

Now 化 was just promoted to a building block. It will appear again in:

```
变化 — change (transform-change)
强化 — strengthen
弱化 — weaken
进化 — evolve
转化 — convert
优化 — optimize
```

That single Hanzi (化) is now a meaning module that activates a dozen words. Every time you encounter a new word ending in 化, you can guess "this means '-ize' or '-ization'."

### The 50 Most Productive Hanzi for MLOps

If you systematically learn these 50 component Hanzi via your 220 vocabulary words, you have unlocked roughly 70-80% of the Hanzi compounding you need:

| Hanzi | Meaning | Appears in |
|-------|---------|------------|
| 模 | model, pattern | 模型, 模板, 模式, 规模 |
| 型 | form, type | 模型, 类型, 型号 |
| 训 | instruct | 训练, 培训, 教训 |
| 练 | practice | 训练, 练习 |
| 推 | push, derive | 推理, 推论, 推荐, 推动 |
| 理 | reason | 推理, 原理, 处理 |
| 量 | measure | 量化, 测量, 增量 |
| 化 | transform, -ize | 量化, 变化, 优化 |
| 部 | section | 部署, 部分, 内部 |
| 署 | place, arrange | 部署, 署名 |
| 集 | gather | 集群, 数据集, 集成 |
| 群 | group | 集群, 用户群 |
| 微 | tiny, fine | 微调, 微服务 |
| 调 | adjust | 微调, 调整, 调用 |
| 参 | reference | 参数, 参考 |
| 数 | number | 参数, 数据, 数量 |
| 算 | calculate | 算力, 计算, 算法 |
| 力 | power | 算力, 能力 |
| 性 | nature, -ness | 性能, 准确性 |
| 能 | ability, can | 性能, 能力, 智能 |
| 速 | speed | 速度, 加速 |
| 度 | degree | 速度, 程度, 角度 |
| 准 | accurate | 准确率, 精准 |
| 确 | certain | 准确率, 精确 |
| 召 | summon | 召回率 |
| 回 | return | 召回率, 回归 |
| 编 | compose, edit | 编码, 编辑 |
| 码 | code | 编码, 解码 |
| 解 | unbind, solve | 解码, 解决 |
| 标 | mark | 标注, 标签, 标准 |
| 注 | note | 标注, 关注 |
| 签 | label, sign | 标签, 签名 |
| 处 | place, handle | 处理, 预处理 |
| 预 | pre-, advance | 预处理, 预训练, 预测 |
| 测 | test | 测试, 测量, 预测 |
| 试 | try, test | 测试, 尝试 |
| 容 | contain | 容器, 容量 |
| 器 | instrument | 容器, 编辑器 |
| 显 | display | 显存, 显卡, 显示 |
| 存 | store | 显存, 存储 |
| 支 | branch, support | 支持, 支撑 |
| 持 | hold | 支持, 保持 |
| 基 | foundation | 基于, 基准, 基础 |
| 于 | at, in | 基于, 用于, 适用于 |
| 用 | use | 用于, 使用, 应用 |
| 通 | through | 通过, 通用 |
| 过 | pass, through | 通过, 经过 |
| 实 | real | 实现, 实际, 实践 |
| 现 | now, appear | 实现, 现在 |
| 提 | raise, mention | 提供, 提升, 提取 |

Memorizing the 220 vocabulary words will expose you to all of these naturally. You do not need to learn the table directly — just be aware that this is the compounding system you are building.

---

## 6. "Don't Memorize. Encounter." — How Frequency Acquisition Works

This is the most important principle in the curriculum, and most learners get it wrong on instinct. Once you have memorized your 220 domain words and start reading real material, unfamiliar words come at you in waves. The naive reaction is: "memorize them all." Wrong reaction.

### Why Brute-Force Memorization Backfires

Suppose you encounter 100 new words this week and force-add them to Anki. A week later your retention rate drops to 50-60%. Why?

1. **Anki has no frequency information.** It treats high-frequency and low-frequency words identically.
2. **Low-frequency words have weak context.** Without repeated encounter in real material, they are essentially random passwords.
3. **Adding 100 cards explodes your review load.** Suddenly you are spending 30 minutes a day on cards instead of 10, and your existing 220 cards weaken from neglect.

### How Frequency Acquisition Actually Works

Natural acquisition follows this loop:

```
You meet a new word in real material (1st time)
  → Look up in Pleco → understand → note it down → keep reading

You meet the same word again (2nd time, days later)
  → "Oh I've seen this" → maybe re-look-up → reinforce

3rd encounter
  → Recognized without lookup

4th-5th encounter
  → Automatic. Word is acquired without ever being in Anki.
```

**The mechanism**: words you meet often = important = acquired automatically. Words you meet rarely = unimportant = no need to learn. Your brain is doing the same thing it did to acquire your native language. Native language acquisition is not "memorization" — it is thousands of repeated encounters.

### Then Why Memorize 220 At All?

The 220 domain words are a **seed for crossing the comprehension threshold**. Below 220 you cannot read, so you cannot encounter words in context, so frequency acquisition cannot start. 220 is the kindling — once it catches, the rest of vocabulary acquisition becomes self-sustaining.

### Workflow When You Encounter a New Word

```
Step 1 — Decompose Hanzi into components and decode each
   Example: 实际上
   实 (real) + 际 (boundary) + 上 (on top)
   → "in reality" / "in fact" — guessable from components

Step 2 — Verify in Pleco
   shí jì shàng — confirmed: "actually, in fact"

Step 3 — Note it (don't add to Anki)
   One-line note in your reading log

Step 4 — Keep reading
   3-5 future encounters → acquired
```

### When to Override the Default and Add to Anki

Default: **don't add encountered words to Anki.**

Exceptions:
- **Brand-new domain abbreviations**: RLHF, MoE, DPO, GRPO, etc. when they are new terms. Add these because they will be central to your reading.
- **Sub-domain vocabulary** specific to your work: autonomous-driving Hanzi if you are in robotics, multimodal Hanzi if you are in vision.
- **Words you have looked up 3+ times and still cannot recall.** Frequency acquisition has failed for these — escalate to manual learning.

These exceptions amount to ~30 cards a month. Manageable.

---

## 7. Self-Diagnostic by Week

Every Sunday, measure:

| Metric | Week 4 target | Week 8 target | Week 12 target |
|--------|---------------|---------------|----------------|
| Anki cards (cumulative) | 220 | 400 | 700 |
| Anki hit rate | 80%+ | 80%+ | 80%+ |
| Time per model-card paragraph | 30 min | 15 min | 5 min |
| DeepL-free comprehension | 30% | 60% | 80% |
| Unknown-word rate in real material | 70%+ | 30% | 10% |

**If you fall behind**:
- Hit rate < 70% → freeze new cards next week, focus on review
- Reading time not improving → revisit Guide 03 (grammar)
- Unknown-word rate not falling → switch reading source (e.g., to your specific sub-domain)

### Three Diagnostic Scenarios

**Scenario A**: Week 4. All 220 cards seen, but hit rate is 65%.

Response: pause new cards entirely. Spend a week on review only. Anki will resurface the weak cards repeatedly until hit rate climbs back to 80%+.

**Scenario B**: Week 8. Reading speed is still 25 minutes per paragraph.

Diagnosis: probably underexposure rather than vocabulary weakness. Increase to two paragraphs of real material per day. Exposure accelerates frequency acquisition more than additional Anki cards do.

**Scenario C**: Week 12. Slump. Progress feels stalled.

Response: take a one-week break, or read non-technical Chinese material (Stellaris wiki, Chinese cooking blogs, anything you actually enjoy). Variety in exposure breaks plateaus.

---

## 8. Slump Management

The slump usually hits Week 5-6 (early Month 2). Reason: you have memorized the 220, but real material reveals that words you do not know vastly outnumber words you do. This feels like progress halted. It is not — it is the threshold-crossing phase.

### Three Responses

**1. Switch to a domain you actually love**

Step away from technical material for a week. Read Chinese material on a topic you would read anyway in English:
- Games — Stellaris Chinese wiki, Magic the Gathering forums
- Cooking — Weibo food posts
- Movies — Douban reviews
- Astrology, hobby topics — whatever

Outside-domain Hanzi exposure speeds up inside-domain acquisition more than people expect.

**2. Re-anchor on the goal**

One GitHub Issue posted in Chinese after 4 months. Imagine it concretely. Which OSS project? What problem? What tone? When the image is sharp, motivation returns.

**3. Re-read your old paragraphs**

Pull up a model-card paragraph you struggled with one month ago. Watch it resolve in 5 minutes that used to take 30. Tangible evidence of progress dissolves slumps.

### Anti-Patterns During Slump

- **Re-memorizing all 220 from scratch**: wastes time. Anki will resurface what is weak.
- **Switching curricula**: another week lost to setup. Slumps last days, not weeks.
- **Quitting**: Week 5-6 is the most common quit point. One more week and you cross.

---

## 9. Graduation + What's Next

When you have read this guide and started memorizing the 220 words, you have begun the vocabulary phase of Month 1. Congrats.

### Month 1 Vocab Graduation Bar

- Anki: 220 cards all encountered
- Anki hit rate: 80%+
- Real model-card paragraph (≈50 characters): readable in 30 min with ≥30% comprehension without DeepL

If all three are met, advance to Month 2.

### What Vocabulary Looks Like After Month 1

Month 2 onward is full frequency-acquisition mode. The 220 stay in Anki for review; everything else is learned by encounter. Guide 04 (Reading Model Cards) walks through this in detail.

### Next Study Guides

- [03 — Grammar Mastery](guide-03-grammar.md)
- [04 — Reading Model Cards](guide-04-model-card.md)

Read Guide 03 (grammar) before starting full-paragraph reading. Vocabulary alone is not enough — without sentence-level structure, you will get stuck even on words you know individually. The 15 grammar patterns plus the 220 words combine to unlock real reading.

Thanks for reading. The path to 220-word mastery should now be clear.
