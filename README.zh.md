# MLOps 中文学习课程

> 一个为期 4 个月的课程，帮助工程师在不学口语的前提下，能直接阅读 DeepSeek / Qwen / 知乎 / CSDN 等中文 MLOps 内容。

[English](README.md) · [한국어 버전](README.ko.md)

---

## 项目缘由

中国正在产出大量前沿的 LLM 与 MLOps 研究，但工程实践层面的深度讨论大多发生在中文圈：ModelScope 上的模型卡、知乎和 CSDN 的故障排查贴、掘金上的工程实践文章。机器翻译能传达表层含义，但在涉及晦涩报错、未公开的模型行为、非官方基准测试等细节时往往失真。

本课程通过**有意排除口语和听力训练**，让学习者在 4 个月内达到能够实用读写中文 MLOps 内容的水平。

## 适合人群

- 有一定编程背景的工程师
- 想**阅读**中文 MLOps 内容、而非进行对话的学习者
- 每个工作日能投入 45 分钟、周末投入 90 分钟，持续 4 个月的人

## 有意排除的内容

- 口语练习
- 听力理解
- 超出基础识别范围的声调记忆
- HSK 应试准备

## 4 个月后达成目标

- 不依赖 DeepL 直接阅读 DeepSeek / Qwen / GLM 官方文档
- 以接近母语速度浏览知乎和 CSDN 技术帖
- 用中文向中国开源项目提交 GitHub Issue
- 在知乎或 CSDN 撰写 300 字以上中文回答

## 课程路线图

| 月份 | 阶段 | 产出 |
|------|------|------|
| Month 1 | 汉字与语法骨架 | 500 汉字 + 15 个核心语法 + 200 个领域词汇 |
| Month 2 | 技术文档阅读 | 5 篇 README + 10 篇论文摘要 |
| Month 3 | 社区内容阅读 | 累计 1,000 汉字 + 累计 400 个领域词汇 |
| Month 4 | 写作与实战 | 提交 1 个 GitHub Issue + 1 篇知乎回答 |

## 仓库结构

```
.
├── README.md              ← 英文 (GitHub 默认)
├── README.ko.md           ← 韩文
├── README.zh.md           ← 中文 (本文件)
│
├── docs/
│   ├── zh/
│   │   ├── grammar.md
│   │   ├── github-issue-template.md
│   │   └── checklist.md
│   ├── en/
│   └── ko/
│
├── vocab/
│   ├── mlops-domain-vocab.csv    ← 多语言主文件
│   └── build/                    ← 各语言生成结果 (gitignored)
│
└── scripts/
    └── build_vocab.py            ← 生成各语言 Anki CSV
```

## 快速开始

```bash
git clone https://github.com/<your-handle>/mlops-chinese-curriculum.git
cd mlops-chinese-curriculum

# 生成各语言的 Anki 导入文件
python3 scripts/build_vocab.py
```

将 CSV 文件导入 Anki：`文件 → 导入 → vocab/build/vocab-zh.csv`。

## 课程详情

### 视频讲座

| # | 标题 | 时长 |
|---|------|------|
| 01 | [为什么会有外国开发者认真学中文](docs/zh/lecture-intro.md) | ~12 分钟 |
| 02 | [为什么海外学员要从领域词汇开始](docs/zh/lecture-02.md) | ~9 分钟 |
| 03 | [为什么 15 个语法句型就够用](docs/zh/lecture-03.md) | ~9 分钟 |
| 04 | [一起精读一篇 ModelScope 模型卡](docs/zh/lecture-04.md) | ~11 分钟 |

以上四讲是导入系列。本课程主要面向海外学员,但中文母语者也可作为参考观看 —— 第 02、03、04 讲都附有「给中文母语者」的补充段落,说明如何写出对海外学员更友好的中文技术文档。

### 学习指南(给海外学员的实际教材)

跟视频讲座配套的长文学习材料。以叙述+大量例子的方式写成,海外学员通读就能跟得上,不是单纯的要点罗列。

| # | 标题 | 分量 |
|---|------|------|
| **00** | **[完全零基础海外学员的起点](docs/zh/guide-00-foundations.md)** | 通读 30-45 分钟 |
| 01 | [学习策略与 4 个月计划](docs/zh/guide-01-curriculum.md) | 通读 30 分钟 |
| 02 | [词汇精通(入门 → 220 词毕业)](docs/zh/guide-02-vocabulary.md) | 通读 45 分钟 + 每周参考 |
| 03 | [语法精通(15 句型从入门到熟练)](docs/zh/guide-03-grammar.md) | 通读 60 分钟 + 每个句型遇到 5 次后再回看 |
| 04 | [精读模型卡(5 段毕业)](docs/zh/guide-04-model-card.md) | 通读 60 分钟 + 每读一篇模型卡参考一次 |

**guide-00 是完全零基础海外学员的入口** —— 解释汉字是什么、部首怎么承载意义、拼音和声调怎么处理。跟中文母语者解释 「外国人学中文是从哪一步开始的」 的最好材料,也在这里面。中文母语者翻一翻 guide-00 大概就懂了。

### 参考文档

- [语法例句集 (15 + 4 个)](docs/zh/grammar.md)
- [GitHub Issue 中文模板](docs/zh/github-issue-template.md)
- [16 周进度清单](docs/zh/checklist.md)

## 关于本课程的说明

本课程主要面向**韩语母语者**设计，因为韩语中的汉字词大幅降低了汉字学习门槛。中文母语者**不需要本课程**——这个仓库的目标读者是想学习中文以阅读中文技术资料的非中文母语开发者。

如果您是中文母语者，欢迎以贡献者身份参与：审阅例句的自然度、补充新兴领域词汇、纠正翻译错误等。

## 工具栈

| 工具 | 用途 | 费用 |
|------|------|------|
| [Anki](https://apps.ankiweb.net/) | 间隔重复记忆 | 免费 (移动端付费) |
| [Pleco](https://www.pleco.com/) | 汉字词典 | 免费 |
| [DeepL](https://www.deepl.com/) | 翻译验证 | 免费 |

## 贡献

欢迎提交 PR：

- 翻译修正 (任何语言)
- 新领域词汇 (特别是 Agent、机器人、多模态等新兴领域)
- 用真实材料中的例句替换虚构例句
- 增加新语言版本

新增词汇时请只修改主文件 `vocab/mlops-domain-vocab.csv`，各语言 CSV 由脚本生成。

## 许可证

MIT — 可自由 fork、修改、再分发。
