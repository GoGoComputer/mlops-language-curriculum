# 02 — Why You Memorize Domain Vocabulary First

> The second video script in this curriculum. Roughly 9 minutes.
> Best watched right before importing `vocab/mlops-domain-vocab.csv` into Anki.

---

## Lecture Script

Hello. This is the second lecture. In the first lecture, I talked about why today is a good day to start reading Chinese. In this lecture, I want to talk about how you actually start it. More specifically — which words you should memorize first.

Do you know what this is? It is an HSK Level 1 vocabulary book. This is the first book most people meet when they begin studying Chinese. When you flip to the first page, what words do you see? 你好 (hello), 我 (I), 你 (you), 再见 (goodbye). Friendly. Then on the second page: 吃 (eat), 喝 (drink), 学校 (school), 朋友 (friend).

Now, if you were going on a vacation to China, those words would be enormously important. But pause for a second. Why are you actually taking this curriculum? To go on vacation? No. You are here because you want to read DeepSeek model cards. You want to find vLLM OOM answers on Zhihu. So is 你好 going to show up there? No. Is 朋友 going to show up there? No.

So I ran a small experiment. I took the first 1,000 characters of the Qwen3 model card on ModelScope and counted how many of those words overlap with the HSK levels. The result? Of all the HSK Level 1 words, only about 25 of them appear in that model card. Twenty-five. Meanwhile, more than 200 words appear in the model card that do not show up anywhere in HSK at all — domain words. So even if you finish the entire HSK Level 1 vocabulary book, you cover roughly 12% of a single model card.

So what do we do? The answer is straightforward. You memorize domain vocabulary first.

What is domain vocabulary? Words like 推理 (inference), 训练 (training), 部署 (deployment), 量化 (quantization), 微调 (fine-tuning), 大模型 (large model), 参数 (parameter). These words are practically nonexistent in everyday conversation. If you walked up to someone in Beijing, said hello, and immediately asked "how is your fine-tuning going," they would think you were strange. But in the first paragraph of any model card, these words come marching out one after another.

And here is where Hanzi starts paying you back. When you learn 推, you do not just unlock 推理 — you also pre-light the way to 推论 (deduction), 推断 (inference, in a different sense), 推荐 (recommendation). When you learn 量, that single character carries you into 量化 (quantization), 增量 (increment), 考量 (consideration), 测量 (measurement). Every Hanzi you commit to memory is a building block that compounds across dozens of technical words. So you are not memorizing 220 isolated words. You are memorizing a few hundred Hanzi blocks that snap into a few thousand technical terms.

And if you happen to be a Korean or Japanese speaker, the leverage gets steeper, because your native vocabulary already shares a large stock of Hanzi-rooted words with Chinese — that is something you can lean into at full weight. But even without that bonus, the compounding effect alone is what makes domain-first vocabulary work.

What does this mean in practice? A general learner who starts with 你好 typically needs about a year before they can begin reading model cards. A learner who starts with domain vocabulary can begin to stumble through the first paragraph of a model card within a month. Roughly a 12x speed-up.

So this curriculum has 220 domain words ready for you on day one. If you open `vocab/mlops-domain-vocab.csv`, you will see five categories: model and architecture, infrastructure and deployment, performance and evaluation, data and pipeline, and general. These 220 words are your one-month target. Import the CSV into Anki, do 30 cards a day, and you finish inside a month.

Now you might ask — well, do I never need to learn everyday vocabulary, then? The answer is — you do not have to actively memorize it. Your goal is not conversation. Your goal is to read model cards. When a word like 实际上 ("in fact") shows up in your reading, you look it up, see the meaning, move on. Do not try to memorize it. After you encounter it five or six times in real material, your brain memorizes it on its own.

This is the most important rule of this curriculum. **Don't memorize. Encounter.** Memorize the 220 domain words deliberately. Let everything else come to you through the reading itself. When you go hiking, you buy hiking boots first. A hundred pairs of regular sneakers will not get you up a mountain. One pair of hiking boots will.

Let me wrap up. First, put the HSK Level 1 vocabulary book aside for now. Second, import `vocab/mlops-domain-vocab.csv` into Anki. Third, finish all 220 words within one month — at 30 cards a day. Fourth, while you are still memorizing, also start reading actual model cards one line at a time, so that the words you just learned land in real material immediately. Words you learn and immediately use are the ones that stick.

In the next lecture, we will talk about — now that you have the words, how do you read sentences? Specifically, why fifteen grammar patterns is enough.

Thank you.

---

## Lecture Structure Notes

| Section | Approx. Time | Core Message |
|---------|--------------|--------------|
| Intro | 0:00 ~ 0:30 | Which words to memorize first |
| HSK Level 1 book | 0:30 ~ 2:00 | The standard learning path's first page |
| Statistical shock | 2:00 ~ 3:00 | HSK1 covers only 12% of a model card |
| Domain vocab definition | 3:00 ~ 4:00 | 推理 / 训练 / 部署 — 220 words |
| Hanzi compounding | 4:00 ~ 5:30 | One Hanzi snaps into dozens of words |
| Anki one-month plan | 5:30 ~ 6:30 | 30 cards a day |
| "Don't memorize, encounter" | 6:30 ~ 8:00 | Everyday vocab comes from reading itself |
| Wrap-up + next lecture | 8:00 ~ 9:00 | Four action items |

## Next Lectures

- 03: Why fifteen grammar patterns is enough — reading grammar vs. speaking grammar
- 04: Reading our first ModelScope model card together
