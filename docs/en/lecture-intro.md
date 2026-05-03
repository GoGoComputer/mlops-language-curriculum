# Intro Lecture — Today is the Day You Should Start Reading Chinese

> The opening video script for this curriculum. Roughly 12 minutes.
> Designed to be read alongside slide narration.

---

## Lecture Script

Hello. This is the MLOps Language Curriculum. This curriculum is a four-month program for engineers who want to read Chinese MLOps content directly. It runs online and all materials are openly available on GitHub. The goal of this curriculum is not to make you a fluent Chinese speaker. The goal is to make you someone who can read the flood of LLM and MLOps content pouring out in Chinese — without going through an English translation. We also want to provide stepping stones, so that someone who is just starting with Hanzi can move on to domain documentation, and someone reading domain documentation can graduate into reading community posts at native pace.

This video is for people who have never studied a foreign language for technical reading before, or for people who used to think reading English was enough. I want to explain why today is a good day to start reading Chinese, and why today is the day you actually have to.

Do you know what this is? It is the Hugging Face homepage. When I first started working with LLMs, model sharing was concentrated at a single address — basically Hugging Face was the entire street. It is still a core platform today, but the atmosphere has shifted. So I sat down and thought about it. Why was model sharing so concentrated in one place back then? Probably because if you were releasing a model, you wanted to put it where the largest English-speaking audience was looking. And users were happy to only have to check one place. So the desire of producers and the desire of consumers met at a single point — a point that happened to lean entirely toward English. That point was Hugging Face.

Because of that, when I first started, English was effectively the lingua franca of ML. arXiv in English. Model cards in English. GitHub READMEs in English. If you could just read English well, you had access to every piece of technical information in the world. And honestly, that was true at the time. New papers came out in English, new frameworks shipped with English documentation, and translations into Korean or other languages took a while to follow. So reading English quickly was, in itself, an information advantage.

So the AI companies we know today — OpenAI, Google DeepMind, Anthropic, Meta AI — were in some sense products of a time when English was the de facto global standard.

Then a very large event happened. The explosion of Chinese open-source LLMs. DeepSeek-V3 dropped at the end of 2024, DeepSeek-R1 followed in 2025, and the LLM ecosystem — which until then had drifted along under the gentle gravity of English-speaking Big Tech — began to lose its balance the moment Chinese models entered.

In the middle of all that, a lot of small changes happened in every corner of the industry. But the change I want to focus on is this: the center of gravity of the source material started to wobble. Or to put it another way, primary information stopped exclusively coming out in English.

So when you look around today, it is genuinely impressive. The DeepSeek team writes their model cards in more detail in Chinese than in English. The Qwen team uploads richer documentation to their ModelScope page than to their English README. On Zhihu, engineers who actually work at the major model labs run troubleshooting threads themselves. On CSDN and Juejin, implementation write-ups appear daily that never make it to the English-speaking internet. And it often takes days, sometimes weeks, before any of it gets cleaned up into English.

This kind of thing was unthinkable back when the OpenAI- and DeepMind-era companies were just getting started. If anyone could pull primary information from non-English sources back then, we called them a research savant. Today, we just call them a good engineer.

The change in the title is what hints at the change in the era. So how did this change actually happen? Did Chinese researchers somehow get smarter in just one or two years? Of course not. As you know, the research capacity of an entire field does not multiply within a single generation. So what caused this change?

I think it is this. The balance of languages in which primary material gets produced has shifted, dramatically. No other field has experienced a more dramatic diversification of primary sources than LLMs, and especially open-source LLMs. And that is probably because in this field, papers, models, code, and community posts all ship at almost the same time — the information cycle is unusually short.

I have prepared a few snapshots that capture this dramatic shift in primary sources. Let us go through them together.

First, there is **ModelScope**. ModelScope is the platform Alibaba built — think of it as the Chinese counterpart to Hugging Face. You will get to know it directly later in this curriculum. If you look here, this is a model card. Model cards used to be just a couple of lines of metadata sitting next to a weights file. Information that you simply could not access in detail before, you can now use very easily. And if you can read these Chinese model cards directly, you can pick up undisclosed benchmarks and quantization options for these powerful models, and put them into your service, your app, or your research, in just a few minutes. What makes that possible is the ability to read Chinese as a primary source.

Then there is **Zhihu**. Zhihu is something like Naver Knowledge-iN crossed with Medium. Zhihu is a body of material on the order of Stack Overflow, but because it operates entirely in Chinese, it is largely invisible to most non-Chinese-speaking engineers. Imagine you are running an inference engine. vLLM is throwing OOM on a particular model and you cannot find an answer in the English GitHub issues. So you are stuck. But from a different angle, you are not stuck — you just searched only in English. And that is a sad kind of stuck, because the answer is sitting somewhere, you just cannot see it. It is not realistic to expect a single engineer outside China to debug a multi-GPU OOM alone in a few weeks. But today, with platforms like Zhihu, if you are running a model and you hit OOM and need to find someone who has hit the same wall, you click into the Chinese-language search and within minutes you are looking at the post of an engineer with a similar GPU setup who walked the same path.

Then there is **GitHub Issue**, which you all already know. In the past, if you were using an open-source model, you had to write the issue in English, wait for a response, and align with the maintainer's time zone — a lot of separate jobs you had to do yourself. With GitHub Issue running on top of all the major Chinese open-source projects, you can now focus on writing the issue clearly in Chinese, and outsource the response, the debugging, and the verification to the maintainer. Of course, to receive a real answer, you do have to write your issue clearly in Chinese yourself.

Then there is the **structure of Hanzi itself**. I think this one is very important. Hanzi is a logographic script. Each character is, in a sense, a tiny blueprint of meaning. When you encounter a new word, what is the first thing your brain does? It tries to guess what the word means and where it might be used.

The same is true here. When you meet a Chinese technical word, you can break it into the component Hanzi, recognize the meaning of each character, and your brain reconstructs the word's meaning piece by piece — often before you have even looked it up. For native Korean and Japanese speakers, who already share a large stock of Hanzi-based vocabulary with Chinese, this is enormously fast. For English speakers, the advantage is smaller but still real — once you have learned the meaning of a Hanzi, that meaning compounds across hundreds of technical words. `推理` (inference) shares its second character with `推论` (deduction), `论文` (paper), `语言模型` (language model), and so on. Learning Hanzi is not learning words one at a time. It is learning a building block that snaps into hundreds of words.

That said, a Chinese sentence is not made of Hanzi alone. Hanzi is the starting point — but word order, function words, measure words, and modal particles all combine to form sentences. So accurately reading any Chinese sentence is not something just anyone can do. But domain vocabulary is different. As soon as you know the Hanzi, the meaning of `量化部署` or `推理时延` snaps into place almost instantly. In domain reading, Hanzi is comprehension. In conversational Chinese, Hanzi is just Hanzi.

That is why the strategy of this curriculum is to learn the Hanzi that appear in MLOps domain vocabulary first, instead of starting from everyday vocabulary. Built around Hanzi recognition, this approach was an obscure trick used by a few self-directed learners not long ago. Today, it is the most important strategy for anyone trying to read Chinese domain content quickly.

The proof is simple. Pick any engineer who reads Chinese MLOps material fluently and ask them whether word order or Hanzi recognition contributed more to their reading speed. The vast majority will say Hanzi recognition. And if you look at the master vocabulary file in this curriculum, fewer than 30% of the entries fall outside the Hanzi-grounded core. That is how big a share Hanzi recognition takes in the learning process.

Everything I have walked you through so far was a sequence of small snapshots — meant to show you that the balance of primary-source production has been violently shaken. The point I am trying to make through all of it is this: today is a good day to start reading Chinese.

Let me change the tone a little.

Here is a graph. The values on it are 100, 5, and 1. What do those numbers mean? You probably cannot guess from that alone. So let me give you a hint. The 100 at the top is the share of LLM primary material in English five years ago. The 1 at the bottom is the share in Korean during the same period, and the 5 in the middle is Chinese. The numbers represent the share of primary LLM content five years ago: English 100, Chinese 5, Korean 1.

Now redraw the same graph for 2025. English is still 100. But Chinese has jumped to roughly 60 or 70. Korean is still around 1. The English material has not shrunk — Chinese material has exploded. DeepSeek shocked the world recently with R1. The team is small. The model is open source. The user base is in the tens of millions, globally.

Yet the primary information you need to actually run such a model lives in the Chinese-language internal wikis and model cards of a small team. Maybe one or two pieces have been cleanly translated into English. There may be a separate English blog post — that adds another piece. The English version may have been comprehensive on day one, but it is unlikely it is being updated as actively as the Chinese original. So if you subtract that, you might be looking at one or two English-language primary sources describing a model that tens of millions of people use. I am being approximate here, of course.

The point is: more than 90% of the primary documentation behind an inference infrastructure used by tens of millions of people exists only in Chinese. That was unimaginable five years ago. And the way this became possible is what I showed you earlier — ModelScope, Zhihu, GitHub issues in Chinese, and the structural advantage of Hanzi recognition. Those forces compounded into a dramatic increase in access to primary information, and the engineers, researchers, and founders who picked up the skill of reading Chinese as a primary source seized the opportunity that opened up.

And if you look at the graph more carefully, the strata at the bottom feed primary information into the strata above. The English-language press cites the Chinese-language primary sources. Think about it. arXiv is an old, respected platform. Zhihu is a hot, busy one. Which one is more famous? You could argue arXiv. But the engineers at Chinese LLM companies are reading Zhihu every single day. And especially because arXiv does not provide troubleshooting information, this is even more so. For real-world debugging, Zhihu may be more useful than arXiv.

Times change, and so do the leading actors. I was somewhat shocked by the result of this graph as I was making it.

It made me think about something. Specifically, the information ecosystem we live in. There used to be effectively one language that ruled it — English. Today, the system is becoming bipolar between English and Chinese. The era of dual-language primary content has arrived.

The clearest example is DeepSeek. The new champion of reasoning models. They publish English papers, but the substantive details live in Chinese blog posts and ModelScope pages. And in a very short period of time, they have made global headlines, as you can see.

There is another rising figure I want to mention. Look at this. It says **Auto-Translated AI News**. I read English-language outlets every day, and every time I look, the share of auto-translated articles ticks up by another notch. And have you ever stopped to think — what about the subtle details that get clipped off in those translations? How are they getting through? Where do they go?

Looked at this way, the space of automatic translation is a place where the convenience of the many has been swapped for the precision of the few. And does this phenomenon only happen in machine translation? The DeepSeek team is brilliant, sure. But machine-translation engines are also competent in their own right. The reason information gets dropped and details get sidelined regardless is **language**.

Information is a question about primary sources, and the strongest primary source today is the original tongue in which something was written. So today, the most important information power, in my view, is the ability to read in the original.

Spear. What comes next? Shield. Spear and shield — the symbol of contradiction.

If you want to start a business and build something significant, you have to know the primary sources. And if you want to protect yourself, your team, and the people you care about from the kind of information asymmetry someone else can wield as a weapon, you also have to know the primary sources. It is a contradiction, but as we all know, that is what reality always feels like — caught between contradictions.

So which language should you actually learn? There are many languages in the world. But they are not all equal in the hierarchy of information. There is a language that governs information — and that language pair is English and Chinese. Among them, the language with the best ratio of effort-to-information-access for a non-Chinese-speaking engineer is Chinese. Or to put it another way: Hanzi recognition.

So what I want to say is: today is the day you have to read Chinese.

So where did all those reading-only foreign-language programs go? They never really existed for technical reading. Conversation schools are everywhere — but a place that teaches you to read MLOps documentation in Chinese, without burning you out on tones and dialogues? That is much rarer. There is a saying that goes — even something as common as a stray dog turns out to be missing the moment you actually need it for medicine. So I started this scrappy little campaign — the MLOps Language Curriculum.

Thank you.

---

## Lecture Structure Notes

| Section | Approx. Time | Core Message | Visual |
|---------|--------------|--------------|--------|
| Intro | 0:00 ~ 1:00 | Curriculum intro, goal (read, don't speak) | Logo |
| Hugging Face throwback | 1:00 ~ 2:30 | The era of single-language primary sources | Old HF homepage |
| The shift event | 2:30 ~ 4:30 | DeepSeek/Qwen explosion, source diversification | DeepSeek-R1 headline |
| Snapshot 1: ModelScope | 4:30 ~ 5:30 | Depth in Chinese model cards | ModelScope screenshot |
| Snapshot 2: Zhihu | 5:30 ~ 6:30 | OOM debugging case | Zhihu troubleshooting thread |
| Snapshot 3: GitHub Issue | 6:30 ~ 7:00 | Writing in Chinese directly | Chinese OSS issue page |
| Snapshot 4: Hanzi structure | 7:00 ~ 8:30 | Hanzi as a building block | Hanzi → composite words diagram |
| The graph | 8:30 ~ 10:00 | EN:ZH primary material ratio shift | Bar chart (5yr ago vs now) |
| Super-individual case | 10:00 ~ 11:00 | DeepSeek as a new power | DeepSeek team / cover photo |
| Auto-translation limits | 11:00 ~ 11:30 | Lost detail | Translation comparison panel |
| Conclusion | 11:30 ~ 12:00 | Today is the day to read Chinese | Campaign slogan |

## Notes for the Slide Deck Builder

- **DeepSeek-V3 / R1 release dates**: December 2024 / January 2025
- **ModelScope card examples**: `Qwen/Qwen3-235B-A22B`, `deepseek-ai/DeepSeek-V3`
- **Zhihu OOM search terms**: `vLLM 显存不够`, `推理 OOM`
- **Hanzi-grounded vocabulary samples**: top 50 entries of `vocab/mlops-domain-vocab.csv`

## Talking Points Specific to English Speakers

The Korean version of this lecture leans heavily on the gift Korean speakers receive from shared Sino-Korean vocabulary. English speakers do not get that gift, so this version compensates in three places:

1. **Honest about Hanzi cost.** Acknowledge upfront that Hanzi recognition is a real investment for English-only learners, not a free shortcut.
2. **Hanzi as building blocks.** Replace the "Sino-Korean intuition" beat with a more universal frame — every Hanzi you learn compounds across hundreds of technical words.
3. **Word-order parity as a quiet upside.** Mandarin is SVO. English speakers who fear word order will find Mandarin syntax less alien than Korean speakers do; the difficulty is concentrated in the script, not the grammar.

## Next Lectures

- 02: Why we start with domain Hanzi instead of everyday Hanzi
- 03: Why 15 grammar patterns is enough — reading grammar vs. speaking grammar
- 04: Reading our first ModelScope model card together
