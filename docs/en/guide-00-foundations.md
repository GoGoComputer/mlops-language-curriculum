# Study Guide 00 — Zero-Stage for Total Beginners

> This guide is for someone who has never studied Chinese before. Read it once before opening any of guides 01-04.
> Nothing to memorize. The goal is a 30-45 minute read that gives you the intuition for "how Chinese actually works."
> All other guides assume you have read this one.

---

## 1. Five Questions This Guide Answers

By the end of this read, you will be able to answer:

1. How is Chinese different from English structurally?
2. What is a Hanzi (Chinese character) and how does it carry meaning?
3. What is pinyin and why do we use it?
4. Do I have to memorize tones?
5. Why does this curriculum take only 4 months for some learners?

You don't need to be able to answer these now. By the end you will.

---

## 2. How Chinese Actually Works

Let us compare directly with English.

In English: "I train the model."

```
I        train         the model
subject  verb          object
```

Same in Chinese:

```
我       训练         模型
wǒ       xùn liàn      mó xíng
I        train         model
```

Three words. No "the." Same Subject-Verb-Object order as English. So far so familiar.

But here is the unusual part: Chinese verbs **do not conjugate**. Whether the action is past, present, future, ongoing, or completed, the verb `训练` stays exactly the same.

| Meaning | Chinese |
|---------|---------|
| I train | 我训练 |
| I trained | 我训练**了** |
| I am training | 我**在**训练 |
| I have trained (before) | 我训练**过** |
| I will train | 我**将**训练 |

The verb body never changes. Tense is carried by helper words like `了 / 在 / 过 / 将`. Once you internalize this, Chinese feels less like a language with weird rules and more like a language with **fewer** rules.

### Three Ways Chinese Differs From English

1. **Writing system.** English uses 26 letters. Chinese uses thousands of Hanzi, where each character carries meaning, not just sound.
2. **No conjugation.** No "-ed," "-ing," "-s." Verbs are invariant.
3. **No articles.** No "a / an / the." Just `模型` for "the model" or "a model" depending on context.

### Where Chinese Is Easier Than You Expect

- **Same word order as English** (SVO). You will rarely have to flip a sentence around.
- **No grammatical gender.** No "der/die/das" or "le/la."
- **No verb agreement.** I, you, he, she, they — all use the same verb form.

---

## 3. What Is a Hanzi (Chinese Character)?

Hanzi are **logographic** — each character represents a meaning unit, not a sound. The English alphabet is the opposite: each letter represents a sound, and you string sounds into words.

### The Most Direct Example

```
木   one tree
林   two trees → woods
森   three trees → forest
```

That is literally how it works. 木 is an abstracted picture of a tree, 林 is two of them, 森 is three. The meaning is encoded into the shape.

Another example:

```
日   sun (a circle representing the sun)
月   moon (a crescent representing the moon)
明   日 + 月 = bright (sun and moon together)
```

Hanzi began as pictures. They became more abstract over thousands of years, but **the meaning hints survive inside the character.**

### Radicals — The Building Blocks Inside Hanzi

Most Hanzi can be decomposed into smaller meaning components called **radicals**. The radical is usually on the left or top of the character, and it tells you the **semantic category**.

Example:

```
推 (to push)  =  扌 (hand)  +  隹 (bird)
                   ↑
              hand radical → "this is a hand action"
```

```
流 (to flow)  =  氵 (three water drops)  +  rest
                   ↑
              water radical → "this is liquid-related"
```

```
烧 (to burn)  =  火 (fire)  +  rest
                   ↑
              fire radical → "this involves heat"
```

```
想 (to think)  =  心 (heart)  +  rest
                    ↑
              heart radical → "mind-related"
```

The 10 most common radicals you will see in MLOps content:

| Radical | Meaning | Hanzi using it |
|---------|---------|----------------|
| 扌 | hand | 推 push, 拉 pull, 打 hit, 接 receive |
| 氵 | water | 流 flow, 海 sea, 河 river |
| 火 | fire | 烧 burn, 炒 stir-fry |
| 心 / 忄 | heart/mind | 想 think, 思 consider, 慢 slow |
| 木 | tree | 树 tree, 林 woods, 森 forest |
| 口 | mouth | 吃 eat, 喝 drink, 听 listen, 说 speak |
| 亻 | person | 你 you, 他 he, 们 (plural) |
| 女 | woman | 好 good, 妈 mom |
| 讠 | speech | 说 speak, 训 instruct, 词 word |
| 阝 | settlement | 部 department, 都 city |

**Do not memorize these.** You will absorb them through exposure. The point of seeing them now is to understand the principle: **a Hanzi is a meaning module made of smaller meaning modules.**

### The Compounding Effect

Here is the consequence — and it is the central reason this curriculum works.

When you learn the Hanzi `推` (push, derive), you do not just learn one word. You unlock dozens:

```
推理   push + reason   = inference
推论   push + theory   = deduction
推断   push + judge    = inference (different sense)
推荐   push + recommend = recommendation
推动   push + move     = drive forward
```

Learn `量` (measure):

```
量化   measure + transform  = quantization
增量   increase + measure   = increment
考量   examine + measure    = consideration
测量   test + measure       = measurement
```

A Hanzi is a building block. **Learning ~500 Hanzi unlocks several thousand technical words by composition.** That is the math behind reading model cards in 6-8 months.

---

## 4. Simplified vs. Traditional Hanzi

Old-style Hanzi, the kind you sometimes see in classical texts or in Hong Kong/Taiwan, are **Traditional (繁體字)** — they have many strokes. In the 1950s, mainland China simplified them. The result is **Simplified (简体字)**.

| Traditional | Simplified | Meaning |
|-------------|-----------|---------|
| 馬 | 马 | horse |
| 學 | 学 | learn |
| 開 | 开 | open |
| 國 | 国 | country |
| 機 | 机 | machine |
| 龍 | 龙 | dragon |
| 體 | 体 | body |

Same characters, different shape. The simplification is mostly a stroke-count reduction.

**ModelScope, DeepSeek, Qwen, Zhihu, CSDN — all Simplified.** Over 99% of MLOps content is Simplified. This curriculum covers Simplified only. You can ignore Traditional entirely.

---

## 5. What Is Pinyin?

Pinyin is **the Roman-letter spelling of Chinese pronunciation**. It is a tool, not the language itself.

Examples:

```
模型  →  mó xíng     ("mo-shing")
推理  →  tuī lǐ      ("tway-lee")
部署  →  bù shǔ      ("boo-shoo")
```

### Why We Use Pinyin

In this curriculum, pinyin has exactly two uses:

1. **To type a Hanzi into your dictionary** (Pleco)
2. **As a rough guess of how a character sounds** (when you encounter a new one)

**You do not need to pronounce anything correctly.** This is a reading curriculum.

### Pinyin Anatomy

A pinyin syllable = **initial (consonant)** + **final (vowel/ending)** + **tone mark**.

Example: `mā`

```
m   +   a   +   ā (1st-tone marker)
initial  final  tone
```

Most consonants are similar to English, but a few are different:

| Pinyin | Approximate sound |
|--------|-------------------|
| zh, ch, sh | English j, ch, sh, but with the tongue curled back slightly |
| z, c, s | "ts" sounds — z is voiced, c is aspirated |
| q | English "ch" but lighter (very front of mouth) |
| x | English "sh" but lighter |
| r | Between English "r" and "j" |

Mastering these pronunciations takes weeks of audio training, which we are deliberately skipping.

**Required**: glance at pinyin and type it into Pleco.
**Not required**: pronounce it correctly.

---

## 6. Tones — Recognize, Don't Drill

Chinese is a **tonal language**. The same syllable, said at different pitches, can mean different things.

`ma` example:

| Tone | Mark | Hanzi | Meaning |
|------|------|-------|---------|
| 1st | mā | 妈 | mother |
| 2nd | má | 麻 | hemp |
| 3rd | mǎ | 马 | horse |
| 4th | mà | 骂 | to scold |
| Neutral | ma | 吗 | (question particle) |

The tone marks visualize the pitch shape:

| Mark | Shape | Mental image |
|------|-------|--------------|
| ā (1st) | flat | high steady |
| á (2nd) | rising | "ah?" — going up |
| ǎ (3rd) | dipping | "aaah" — down then up |
| à (4th) | falling | "ah!" — sharp down |
| a (neutral) | none | light, short |

### What You Need vs. Don't Need

**Need**: Recognize tone marks visually so you can type pinyin into Pleco.
**Don't need**: Pronounce tones correctly. Hear and distinguish tones in speech.

This is a reading curriculum. Tones become a typing affordance, not a speaking obligation.

---

## 7. Quick Comparison Summary

| Aspect | English | Chinese |
|--------|---------|---------|
| Writing | Roman alphabet, phonetic | Hanzi, logographic |
| Word order | SVO | SVO ✓ same |
| Verb conjugation | Yes (-ed, -ing, -s) | No, ever |
| Tense marking | Verb conjugation | Auxiliary words (了, 过, 将, 在) |
| Articles | a/an/the | None |
| Tones | None | Five (incl. neutral) |
| Plurals | -s endings | Usually none, sometimes 们 |

The aspects that look unfamiliar (no conjugation, no articles, tones) are mostly subtraction, not addition. Chinese has fewer rules in many places — you just need to internalize the rules it does have.

---

## 8. The Compounding Bonus for Korean and Japanese Speakers

You should know about a structural advantage some learners have, because if you ever pair-program with a Korean or Japanese teammate learning the same way, they will be moving faster — and there is a real reason.

About 70% of Korean vocabulary and a similarly large slice of Japanese vocabulary is **Sino-Korean / Sino-Japanese** — words built from Hanzi shared with Chinese. So when a Korean learner sees `部署`, they recognize it instantly as cognate to a Korean word meaning "department/deployment." That is a free year of vocabulary.

You as an English speaker do not get this. **Your equivalent leverage is Hanzi decomposition.** Every Hanzi you learn compounds across dozens of words. The Korean speaker gets 220 words almost for free; you get 220 words by learning ~500 Hanzi components — slower at first, but the same destination.

This curriculum's main timeline (4 months) is calibrated for Korean speakers. As a pure English speaker, plan on 6–8 months. Same content, just more time on Hanzi-block consolidation.

---

## 9. Your First 10 Hanzi — Decomposition Walkthrough

Let us decompose 10 of the most common MLOps Hanzi. The point is not to memorize them — it is to **internalize the decomposition workflow.**

| Hanzi | Pinyin | Radical | Decomposition | Meaning |
|-------|--------|---------|---------------|---------|
| 模 | mó | 木 (tree) | 木 + 莫 → "modeled in wood" | model, pattern |
| 型 | xíng | 土 (earth) | 土 + 刑 → "shape cast in clay" | form, type |
| 推 | tuī | 扌 (hand) | hand + 隹 (bird) → "push with hand" | push, derive |
| 理 | lǐ | 王 (jade) | jade + 里 → "the grain of jade" | logic, reason |
| 训 | xùn | 讠 (speech) | speech + 川 (flow) → "instruct with flowing words" | instruct, train |
| 练 | liàn | 纟 (silk) | silk + 柬 → "sort silk threads" | practice, drill |
| 部 | bù | 阝 (place) | 立 + 阝 → "divide into sections" | section, department |
| 署 | shǔ | 罒 (net) | net + 者 → "bureau, place" | place, arrange |
| 量 | liàng | 里 (village) | 旦 (sun) + 里 → "measurement unit" | quantity, measure |
| 化 | huà | 亻 (person) | person + 匕 → "transformation" | change, -ize |

### Watch Them Compound Into Domain Words

```
模 + 型  =  模型     →  model
推 + 理  =  推理     →  inference
训 + 练  =  训练     →  training
部 + 署  =  部署     →  deployment
量 + 化  =  量化     →  quantization
```

**Key insight**: Once you know around 100 high-frequency Hanzi, you can guess the meaning of about 1,000 multi-character words. Hanzi are bricks; words are buildings.

---

## 10. Your First 5 Words — From Cold-Start to Comprehension

Here is the actual workflow your brain runs when you encounter a new word in real material. Once you do this 30 or so times, it becomes near-instant.

### Example 1: 训练

```
1. Identify Hanzi:        训 + 练
2. Identify radicals:     讠 (speech) + 纟 (silk)
3. Decompose meaning:     "instruct with words" + "sort silk" → discipline, drill
4. Cross-check pinyin:    xùn liàn — sounds like "shoon-lyen"
5. Conclude:              training ✓
```

### Example 2: 部署

```
1. Identify Hanzi:        部 + 署
2. Identify radicals:     阝 (place) + 罒 (net)
3. Decompose meaning:     "divide into sections" + "place / arrange"
4. Cross-check pinyin:    bù shǔ
5. Conclude:              deployment ✓
```

### Example 3: 量化

```
1. Identify Hanzi:        量 + 化
2. Identify radicals:     里 (measure) + 亻 (person, usually action marker)
3. Decompose meaning:     "measure" + "transform" = transform into measurable units
4. ML domain context:     reducing weights to lower-bit representation
5. Conclude:              quantization ✓
```

### Example 4: 微调

```
1. Identify Hanzi:        微 + 调
2. Decompose meaning:     "subtle/tiny" + "adjust"
3. Conclude:              fine-tuning ✓
```

### Example 5: 推理

```
1. Identify Hanzi:        推 + 理
2. Identify radicals:     扌 (hand) + 王 (jade)
3. Decompose meaning:     "push" + "reason" = derive by pushing through reasoning
4. ML domain context:     running a trained model on new input
5. Conclude:              inference ✓
```

After about 30 reps of this five-step workflow, your brain compresses it. New words start resolving in 1-2 seconds. That compression is what guide 02's "220 vocab in one month" target is actually measuring.

---

## 11. Where to Go Next

If you have read through this guide once, you are ready to start the real curriculum.

**Recommended path:**

1. (Optional) Watch the 4 lecture videos — see the [Lecture series in the README](../../README.md#lecture-series)
2. **[Study Guide 01 — Strategy and the 4-Month Plan](guide-01-curriculum.md)** ← real start
3. [Study Guide 02 — Vocabulary Mastery](guide-02-vocabulary.md) ← 220 words
4. [Study Guide 03 — Grammar Mastery](guide-03-grammar.md) ← 15 patterns
5. [Study Guide 04 — Reading Model Cards](guide-04-model-card.md) ← practice

**This zero-stage guide is not a memorization target.** A single read, building intuition. The actual learning starts in guide 02.

---

## FAQ

**Q. Should I memorize radicals?**
A. No. Recognize the 10–20 most common ones from exposure. Pleco shows you the radical for any character automatically.

**Q. Will I be able to pronounce things correctly without tone practice?**
A. No, and that is intentional. Pronunciation is for speakers; we are readers.

**Q. How many Hanzi will I know by graduation?**
A. ~1,000 cumulative by Month 3. Combined with the 220-word domain vocabulary, that covers >80% of any MLOps document.

**Q. What if I am a complete beginner with no Hanzi exposure at all?**
A. That is the assumption of this guide. Read this once, then jump straight to guide 01. The pace is calibrated for cold-start learners; you do not need any prior exposure.

**Q. Is this curriculum any good for someone who wants to also learn to speak?**
A. Not really. We deliberately exclude speaking and listening. If your goal includes conversation, pair this with a 6–12 month parallel speaking program (HelloChinese, italki tutor).

**Q. How long does this guide take to read?**
A. 30–45 minutes. Don't try to memorize anything. The point is the gestalt.
