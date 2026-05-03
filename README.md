# MLOps Chinese Curriculum

> A 4-month curriculum for engineers who want to read DeepSeek / Qwen / Zhihu / CSDN technical content in Chinese — without learning to speak it.

[한국어 버전](README.ko.md) · [中文版](README.zh.md)

---

## Why this exists

China is producing a huge share of state-of-the-art LLM and MLOps research, but most of the practitioner-level discussion happens in Chinese — model cards on ModelScope, troubleshooting threads on Zhihu and CSDN, and engineering writeups on 掘金. Machine translation handles surface meaning but loses nuance, especially around obscure errors, undocumented model behaviors, and unofficial benchmarks.

This curriculum gets you to **functional reading and writing fluency** for Chinese MLOps content in 4 months, by deliberately excluding speaking and listening.

## Who this is for

- Engineers with some programming background
- People who want to **read** Chinese MLOps content, not have conversations
- Learners willing to spend ~45 minutes per weekday + 90 minutes on weekends

## What's excluded (intentionally)

- Speaking practice
- Listening comprehension
- Tone memorization beyond basic recognition
- HSK exam preparation

## What you'll achieve

By the end of 4 months:

- Read DeepSeek / Qwen / GLM official documentation without DeepL
- Browse Zhihu and CSDN technical posts at native pace
- Submit a GitHub Issue in Chinese to a Chinese open-source project
- Write a 300+ character answer on Zhihu or CSDN

## Roadmap

| Month | Phase | Output |
|-------|-------|--------|
| 1 | Foundations | 500 hanzi + 15 grammar patterns + 200 domain words |
| 2 | Tech doc reading | 5 READMEs + 10 paper abstracts read |
| 3 | Community reading | 1,000 cumulative hanzi + 400 cumulative domain words |
| 4 | Writing & shipping | GitHub Issue + Zhihu post submitted |

## Repository structure

```
.
├── README.md              ← English (default)
├── README.ko.md           ← Korean
├── README.zh.md           ← Chinese
│
├── docs/
│   ├── en/
│   │   ├── grammar.md
│   │   ├── github-issue-template.md
│   │   └── checklist.md
│   ├── ko/                ← Same files in Korean
│   └── zh/                ← Same files in Chinese
│
├── vocab/
│   ├── mlops-domain-vocab.csv     ← Master multilingual file
│   └── build/                     ← Generated per-language CSVs (gitignored)
│
└── scripts/
    └── build_vocab.py             ← Build per-language Anki CSVs
```

## Quick start

```bash
git clone https://github.com/<your-handle>/mlops-chinese-curriculum.git
cd mlops-chinese-curriculum

# Generate per-language Anki-importable vocab CSVs
python3 scripts/build_vocab.py

# Output appears in vocab/build/
#   vocab-ko.csv  ← Front: hanzi | Back: Korean (pinyin)
#   vocab-en.csv  ← Front: hanzi | Back: English (pinyin)
#   vocab-zh.csv  ← Front: hanzi | Back: pinyin only
```

Import the CSV into Anki: `File → Import → vocab/build/vocab-en.csv`. Set Front field to "front" and Back field to "back".

## Difficulty by native language

This curriculum is calibrated for **Korean speakers** because the author is Korean. Adjust your timeline:

| Native language | Reason | Suggested timeline |
|-----------------|--------|--------------------|
| Korean | Sino-Korean vocabulary gives ~50% headstart on hanzi | 4 months ✓ |
| Japanese | Shared kanji, but different readings | 4–5 months |
| English / European | No hanzi familiarity | 6–8 months |
| Chinese (already) | You don't need this curriculum | 0 months |

If you're an English speaker following this curriculum, **double the hanzi targets** in Month 1 and add 2 extra months between Month 1 and Month 2.

## Curriculum detail

### Lecture series

| # | Title | Length |
|---|-------|--------|
| 01 | [Today is the Day You Should Start Reading Chinese](docs/en/lecture-intro.md) | ~12 min |
| 02 | [Why You Memorize Domain Vocabulary First](docs/en/lecture-02.md) | ~9 min |
| 03 | [Why Fifteen Grammar Patterns Is Enough](docs/en/lecture-03.md) | ~9 min |
| 04 | [Reading Our First ModelScope Model Card Together](docs/en/lecture-04.md) | ~11 min |

The four lectures above are an orientation series — watch each one before starting the corresponding phase. In order, they cover why a reading-only learning path is viable (intro), where to start memorizing (02), how far grammar needs to go (03), and how to disassemble a real model card (04).

### Study guides (the actual coursework)

Long-form study guides that pair with the lecture videos. Written to be readable end-to-end — narrative explanations with worked examples, not just bullet points.

| # | Title | Length |
|---|-------|--------|
| **00** | **[Zero-Stage for Total Beginners](docs/en/guide-00-foundations.md)** | 30-45 min read |
| 01 | [Strategy and the 4-Month Plan](docs/en/guide-01-curriculum.md) | 30 min read |
| 02 | [Vocabulary Mastery (onboarding → 220-word graduation)](docs/en/guide-02-vocabulary.md) | 45 min read + weekly reference |
| 03 | [Grammar Mastery (15 patterns, intro → deep)](docs/en/guide-03-grammar.md) | 60 min read + revisit per pattern |
| 04 | [Reading Model Cards (5-paragraph graduation)](docs/en/guide-04-model-card.md) | 60 min read + per-card reference |

**Guide 00 is the entry point for learners who have never seen Chinese before.** It walks you through what Hanzi are, how radicals carry meaning, how pinyin and tones work — at the level needed to start guide 02 without being lost. Read it once before opening guides 01-04.

### Reference documents

- [Grammar examples (15 patterns + 4 bonus)](docs/en/grammar.md)
- [GitHub Issue templates in Chinese](docs/en/github-issue-template.md)
- [Weekly progress checklist](docs/en/checklist.md)

## Tools

| Tool | Purpose | Cost |
|------|---------|------|
| [Anki](https://apps.ankiweb.net/) | Spaced repetition for hanzi & vocab | Free (mobile paid) |
| [Pleco](https://www.pleco.com/) | Hanzi dictionary (essential) | Free |
| [DeepL](https://www.deepl.com/) | Translation verification only | Free |
| [Immersive Translate](https://immersivetranslate.com/) | Browser bilingual overlay | Free |
| HelloChinese | Pinyin basics (Week 1 only) | Free |

## Contributing

PRs welcome for:

- Translation corrections (any language)
- New domain vocabulary (especially in emerging areas: agents, robotics, multimodal)
- Real-world examples replacing fabricated ones
- Additional language versions (Japanese, Vietnamese, etc.)

When adding vocab, edit only `vocab/mlops-domain-vocab.csv` (the master file). Per-language CSVs are generated.

## License

MIT — fork, modify, redistribute freely.
