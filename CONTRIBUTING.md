# Contributing

Thanks for considering a contribution. This curriculum is meant to grow as practitioners use it.

## What's most welcome

- **Translation corrections** in any of the three language versions (ko / en / zh)
- **New domain vocabulary**, especially in fast-moving areas: agents, robotics, multimodal, on-device inference
- **Real examples** that can replace fabricated ones (with source link)
- **Additional language versions** (Japanese, Vietnamese, etc.)
- **Bug reports** in `scripts/build_vocab.py`

## Vocabulary additions

Edit only `vocab/mlops-domain-vocab.csv`. Per-language CSVs are generated.

Required columns:

| Column | Example | Notes |
|--------|---------|-------|
| `hanzi` | `推理` | Simplified Chinese |
| `pinyin` | `tuī lǐ` | With tone marks, space-separated |
| `ko` | `추론` | Korean translation |
| `en` | `inference` | English translation |
| `category_zh` | `模型与架构` | One of: 模型与架构 / 基础设施与部署 / 性能与评估 / 数据与流水线 / 通用 |
| `category_ko` | `모델·아키텍처` | Matching Korean category |
| `category_en` | `Models & Architecture` | Matching English category |
| `tags` | `mlops llm` | Space-separated tags |

After editing, regenerate per-language CSVs:

```bash
python3 scripts/build_vocab.py
```

## Translation corrections

If you find an awkward sentence or wrong translation in any docs file:

1. Open a PR with the fix
2. In the PR description, briefly explain why the change is more natural
3. If you're a native speaker of the target language, mention that — it speeds review

## Adding a new language

To add language `xx` (e.g., `ja` for Japanese):

1. Add columns `xx` and `category_xx` to `vocab/mlops-domain-vocab.csv`
2. Add a `LANGS["xx"]` entry to `scripts/build_vocab.py`
3. Create `docs/xx/{grammar,github-issue-template,checklist}.md`
4. Add `README.xx.md` and link it from the other README files

## Pull request style

- One change per PR (don't mix translation fixes with vocab additions)
- Keep commit messages descriptive: `Fix awkward Korean phrasing in grammar.md` is better than `update`
- Translation PRs from native speakers don't need extensive justification

## Code of conduct

Be respectful. Many contributors will be non-native speakers of the language they're improving — patient feedback helps everyone.
