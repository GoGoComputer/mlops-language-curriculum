# Weekly Checklist — 4-Month MLOps Chinese

> Spend 5 minutes every Sunday evening checking off items. Don't roll incomplete items forward — instead, do a 1-hour catch-up session that Sunday.

---

## Month 1 — Foundations

### Week 1: Pinyin + hanzi recognition system

- [ ] Complete HelloChinese pinyin chapter (within 3 days)
- [ ] Build a sense of Korean-hanja ↔ simplified-Chinese mapping (e.g., 模型 → 모형 → model — applies if you know Korean; English speakers can skip)
- [ ] One pass of 4-tone audio discrimination (then ignore tones)
- [ ] At least 30 minutes of study, 5+ days

**Deliverable**: Can guess the pronunciation of a README paragraph without consulting the pinyin chart.

---

### Week 2: 300 common hanzi (first pass)

- [ ] Set up Anki deck "HSK 1-3 Hanzi Frequency"
- [ ] 50 hanzi × 6 days + 1 day review = 300 hanzi exposed
- [ ] Mark hanzi already inferable from prior knowledge (pass quickly)
- [ ] Install Pleco app and learn its lookup interface

**Deliverable**: 60%+ recognition rate on HSK 1-3 hanzi.

---

### Week 3: 15 core grammar patterns

- [ ] Read through `docs/en/grammar.md` once
- [ ] Create 1 Anki card per pattern (15 cards total)
- [ ] Memorize 1 of the 3 examples per pattern
- [ ] Verify 5 of your own example sentences with DeepL

**Deliverable**: Can explain meaning and structure of all 15 patterns on sight.

---

### Week 4: 200 MLOps domain vocab (first pass)

- [ ] Generate Anki CSV: `python3 scripts/build_vocab.py --lang en`
- [ ] Import `vocab/build/vocab-en.csv` into Anki
- [ ] One pass through Models & Architecture (~70 words)
- [ ] One pass through Infrastructure & Deployment (~50 words)
- [ ] One pass through Performance + Data categories (~40 words)
- [ ] Attempt the first paragraph of DeepSeek README (target: 30% comprehension)

**Deliverable**: 50%+ recognition rate on the 220 domain vocab cards.

---

### Month 1 final check

- [ ] Cumulative hanzi: 300
- [ ] All 15 grammar patterns mastered
- [ ] First pass of all 220 domain vocab complete
- [ ] DeepSeek/Qwen README first paragraph: 30% comprehension
- [ ] HelloChinese graduated (don't use again)

**If incomplete**: Add 1 catch-up week before starting Month 2.

---

## Month 2 — Tech Doc Reading

### Week 5: Tech README intro

- [ ] Carefully read DeepSeek-V3 GitHub README (mark sentences)
- [ ] Carefully read Qwen2.5 GitHub README
- [ ] Add unknown words to Anki (target: 30+)
- [ ] Compare your literal translation against DeepL — note differences

**Deliverable**: 50%+ comprehension on both READMEs.

---

### Week 6: Additional grammar + academic style

- [ ] Learn: serial verb constructions / `所` + verb / `即` `如` `亦`
- [ ] Anki cumulative unknown words: 50+
- [ ] Read 3 Chinese paper abstracts (jiqizhixin.com)
- [ ] Identify `对...进行` `基于` `用于` patterns in real docs ✓

**Deliverable**: Can recognize 5+ academic-style fixed expressions on sight.

---

### Week 7: Model cards & tutorials

- [ ] Read 3 Chinese model cards on HuggingFace
- [ ] Read 2 ModelScope model cards
- [ ] Read 1 ChatGLM or Qwen official tutorial completely
- [ ] Cumulative domain vocab: 300

**Deliverable**: Can immediately parse the standard model-card structure (purpose / input / output / limitations).

---

### Week 8: Conquering paper abstracts

- [ ] Read 5 Chinese abstracts across different fields
- [ ] List 10 fixed expressions that recur in papers
- [ ] DeepL dependency drops below 50%
- [ ] Month 2 evaluation: read a full README page within 30 minutes

**Deliverable**: 70% comprehension of a paper abstract paragraph in 5 minutes.

---

### Month 2 final check

- [ ] Cumulative hanzi: 600
- [ ] Cumulative domain vocab: 300
- [ ] 5 DeepSeek/Qwen READMEs read in detail
- [ ] 10 Chinese paper abstracts read
- [ ] First-pass reading without DeepL is feasible (DeepL only for verification)

---

## Month 3 — Community Reading

### Week 9: Entering Zhihu

- [ ] Create Zhihu account, install Immersive Translate extension
- [ ] Read 2 Zhihu posts/day × 7 days = 14 posts on `大语言模型` topic
- [ ] Compile 10 common community slang/abbreviations (e.g., `yyds`, `nb`)
- [ ] Anki: 50+ new words

**Deliverable**: Read a Zhihu answer in 30 minutes with 70% comprehension.

---

### Week 10: CSDN troubleshooting

- [ ] Read 2 CSDN posts/day × 7 days
- [ ] Identify the standard troubleshooting structure (问题·分析·解决)
- [ ] Catalog Chinese developer comment patterns
- [ ] Cumulative domain vocab: 350

**Deliverable**: Can identify the core fix in a troubleshooting post within 1 minute.

---

### Week 11: 掘金 + tech news

- [ ] 1 Juejin post + 1 Jiqizhixin article per day
- [ ] Compile 20 trending Chinese tech keywords (e.g., `具身智能` `世界模型`)
- [ ] Reading rate without Immersive Translate reaches 50%
- [ ] Cumulative domain vocab: 400

**Deliverable**: Can summarize Chinese AI industry trends in English in 5 minutes.

---

### Week 12: Integration + 1,000 cumulative hanzi

- [ ] Add HSK 4 hanzi (target: 1,000 cumulative)
- [ ] Stabilize 2 posts/day routine across Zhihu/CSDN/Juejin
- [ ] Unknown word frequency: ≤5 per page
- [ ] Month 3 evaluation: 80% comprehension on a fresh article

**Deliverable**: First-pass reading of general tech articles requires no DeepL.

---

### Month 3 final check

- [ ] Cumulative hanzi: 1,000
- [ ] Cumulative domain vocab: 400
- [ ] 4-week sustained routine of 2 posts/day across Chinese platforms
- [ ] DeepL reduced to verification-only

---

## Month 4 — Writing & Shipping

### Week 13: Internalize writing templates

- [ ] Read through all 8 templates in `docs/en/github-issue-template.md`
- [ ] Memorize 30 common one-liners
- [ ] Write 3 fake bug reports for practice (don't submit)
- [ ] Verify your writing with DeepL — note awkward spots

**Deliverable**: Can write a standard bug report within 30 minutes.

---

### Week 14: Real practice — writing answers

- [ ] Find 5 questions on Zhihu or CSDN you can answer
- [ ] For each: draft in your native language → translate to Chinese → polish
- [ ] **Actually post one** (300+ characters)
- [ ] Monitor responses

**Deliverable**: 1 Chinese answer posted to Zhihu or CSDN ✅

---

### Week 15: Real practice — writing Issues

- [ ] Read 20 existing issues on DeepSeek or Qwen repos
- [ ] Pick 1 actual problem you've encountered while using their model
- [ ] Draft using the standard template
- [ ] Verify natural tone (round-trip translate via DeepL: zh ↔ en)
- [ ] **Actually submit it**

**Deliverable**: 1 GitHub Issue submitted in Chinese ✅

---

### Week 16: Wrap-up + self-assessment

- [ ] Read a fresh README without DeepL, self-rate comprehension
- [ ] Compile cumulative hanzi/vocab statistics
- [ ] Write a 4-month retrospective in your native language
- [ ] Decide next steps: HSK 5 / graduate / add listening / etc.

**Deliverable**: Retrospective + next-step plan.

---

### Month 4 final check (graduation criteria)

- [ ] **GitHub Issue or Discussion submitted in Chinese** ✅
- [ ] **Zhihu answer or CSDN post published in Chinese** ✅
- [ ] First-pass reading without DeepL (DeepL only for verification)
- [ ] Cumulative: 1,000 hanzi + 400 domain vocab
- [ ] Daily Chinese AI community monitoring habit established

---

## Daily routine (Mon–Fri)

```
45 minutes daily ─────────────
  ├─ 10 min: Anki review (hanzi + vocab)
  ├─ 20 min: Read 1 tech doc / community post
  ├─ 10 min: Add unknown words to Anki
  └─  5 min: DeepL verification
──────────────────────────────
```

## Weekend routine (one of Sat/Sun)

```
90 minutes weekly ─────────────
  ├─ 30 min: Cumulative weekly word review
  ├─ 30 min: Long-form reading (paper abstracts, long READMEs)
  ├─ 20 min: Writing practice (notes, fake issues)
  └─ 10 min: Weekly checklist review
───────────────────────────────
```

---

## Progress tracking table

| Week | Cum. hanzi | Cum. vocab | Sources read | DeepL dependency | Notes |
|------|------------|------------|--------------|------------------|-------|
| W1   |            |            |              |                  |       |
| W2   |            |            |              |                  |       |
| W3   |            |            |              |                  |       |
| W4   |            |            |              |                  |       |
| W5   |            |            |              |                  |       |
| W6   |            |            |              |                  |       |
| W7   |            |            |              |                  |       |
| W8   |            |            |              |                  |       |
| W9   |            |            |              |                  |       |
| W10  |            |            |              |                  |       |
| W11  |            |            |              |                  |       |
| W12  |            |            |              |                  |       |
| W13  |            |            |              |                  |       |
| W14  |            |            |              |                  |       |
| W15  |            |            |              |                  |       |
| W16  |            |            |              |                  |       |

---

## Slump response

- **Missed targets 2 weeks in a row**: Reduce volume to 70% and take 1 catch-up week
- **Lost interest**: Spend 1 week on Chinese material in a personally interesting domain (gaming wikis, fiction, hobby forums) for variety
- **Over-reliant on translator**: Don't quit cold turkey. Just keep the principle: "first pass yourself → DeepL only when stuck"
- **3+ weeks of no progress**: Re-tune the curriculum. If hanzi < 600, prioritize hanzi over vocab

---

## After graduation

Once both graduation outputs are completed, the curriculum is done. Next options:

1. **Maintenance mode** — 15 min/day Anki + 1 article/week to prevent decay
2. **Expansion mode** — Add HSK 5 hanzi + listening (if business travel/meetings are likely)
3. **Practitioner mode** — Become a contributor to a Chinese open-source project
