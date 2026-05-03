# 03 — Why Fifteen Grammar Patterns Is Enough

> The third video script in this curriculum. Roughly 9 minutes.
> Best watched right before opening `docs/en/grammar.md`.

---

## Lecture Script

Hello. This is the third lecture. In the second lecture, I told you to memorize 220 domain words within one month. In this lecture, I want to talk about — now that you have words, how do you read sentences? In other words, why fifteen grammar patterns is enough.

Let me start with a question. Are you fluent in spoken English? Be honest. If you said no — let me ask the next question. But you read English READMEs, right? Most non-native English-speaking engineers would say no to the first question and yes to the second. Same person.

This is actually a very strange thing if you think about it. How can someone who cannot hold a conversation in English read a technical README in English without much trouble? The answer is surprisingly simple. **Speaking grammar and reading grammar are practically different domains.** Speaking has the patterns that show up in speaking. Reading has the patterns that show up in reading. And the overlap between those two domains is much smaller than people assume.

Now let us bring this to Chinese. The most important grammar in Chinese conversation is probably the family of mood particles — 吧, 啊, 呢, 嘛 and friends. These do not have a clean equivalent in English. They sit at the end of a sentence and add a subtle nuance. 你来吧 means "come on, come over." 你来啊 means more like "come, won't you?" 你来呢 means "as for you coming, what about that?" They look almost identical, but the tone is different. Mastering them is the heart of conversational grammar.

Now, do these mood particles ever show up in a ModelScope model card? They do not. Not 吧, not 啊. Why? Because technical documentation is not transmitting a speaker's emotion — it is transmitting facts. Mood particles do not appear at all.

So what grammar actually shows up in a model card? Let me give you the top five.

First, **把** — the disposal construction. "Dispose of X by doing Y to it." `把模型转换为 ONNX 格式`. — "Convert the model to ONNX format." If you are coming from English, this is the "convert X to Y" pattern. It shows up everywhere in code-walkthrough sentences.

Second, **将** — the formal/written-register version of 把. In official docs and papers, 将 is the standard, not 把. `将参数初始化为 0`. — "Initialize the parameters to 0."

Third, **用于** — "is used for." `该模型用于文本生成`. — "This model is used for text generation." This appears in roughly the first sentence of every README.

Fourth, **基于** — "based on." `基于 Transformer 架构`. — "Based on Transformer architecture." Never absent from a model introduction.

Fifth, **对...进行** — "perform Y on X." `对模型进行量化`. — "Perform quantization on the model." This is genuinely high-frequency. Treat it as a fixed expression of the technical register.

Just these five will get you through about half of a model card. Add ten more — 是...的 (emphasis), 不/没 (negation), 可以/能 (capability), 如果...就 (conditional), 通过 (by means of), 需要 (need), 支持 (support), 被 (passive), serial-verb constructions, and 得 (degree complement) — and you have fifteen. With those fifteen, you can resolve more than 80% of model cards and READMEs.

Are these fifteen good for conversation? Not really. If you tried to speak using only these patterns, you would sound like a stiff Chinese-learning bot. But that is not the point. We are not trying to have conversations. We are trying to read model cards. So patterns that are inefficient for speaking turn out to be the precise tools for what we are doing.

One more piece of good news. Mandarin word order is SVO — same as English. 我吃饭 maps directly to "I eat rice." If you are coming from a language with SOV order, you might find this slightly disorienting at first. But if you regularly read English, you can simply borrow the English word order. Do not worry about whether it will become natural — read one paragraph of a model card every day for a month, and word order stops being something you have to think about. This is learned by exposure, not memorization.

Let me wrap up. First, set conversational grammar aside. You can ignore 吧, 啊, 呢, 嘛 entirely for now. Second, start by memorizing 把, 将, 用于, 基于, 对...进行 — those five. They cover half. Third, the remaining ten are laid out for you in `docs/en/grammar.md`. Fourth, word order is not memorized — it is absorbed. Read one paragraph of a model card every day.

In the next lecture, we will take the 220 words and the 15 patterns we now have, and read our first ModelScope model card together. The real practice begins.

Thank you.

---

## Lecture Structure Notes

| Section | Approx. Time | Core Message |
|---------|--------------|--------------|
| Intro | 0:00 ~ 0:30 | The justification for 15 patterns |
| English analogy | 0:30 ~ 1:30 | You read READMEs without speaking |
| Speaking vs reading grammar | 1:30 ~ 2:30 | Mood particles do not appear in model cards |
| Top 5 patterns | 2:30 ~ 6:00 | 把 / 将 / 用于 / 基于 / 对...进行 |
| Remaining 10 + 80% coverage | 6:00 ~ 7:00 | Pointer to grammar.md |
| Word order (SVO) | 7:00 ~ 8:00 | Same as English |
| Wrap-up + next lecture | 8:00 ~ 9:00 | Four action items |

## Next Lecture

- 04: Reading our first ModelScope model card together
