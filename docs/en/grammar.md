# 15 Core Grammar Patterns — Real-World Examples

> Patterns that actually appear in Chinese tech READMEs, papers, and community posts.
> Each entry: **pattern → meaning → 3 examples → English translation → learning notes**

---

## 1. `是...的` — copular emphasis

**Meaning**: Emphasizes the nature, time, manner, or agent of an action. In tech writing, this is the core pattern for "this model is built using X" type statements.

**Examples**
- 这个模型**是**基于 Transformer 架构**的**。
  → This model **is** built on the Transformer architecture.
- 该项目**是**用 PyTorch 实现**的**。
  → This project **is** implemented in PyTorch.
- 这些参数**是**在预训练阶段确定**的**。
  → These parameters **are** determined during the pre-training phase.

**Note**: The emphasized element sits between `是` and `的`. Roughly equivalent to English cleft sentences ("It is X that...").

---

## 2. `不 / 没` — negation

**Meaning**: `不` = general/future negation. `没` = "did not happen" / "do not have" (past or completion negation).

**Examples**
- 当前版本**不**支持 Windows 系统。
  → The current version does **not** support Windows.
- 该参数**没**有默认值，必须显式指定。
  → This parameter has **no** default value and must be explicitly specified.
- 我**没**遇到过这个错误。
  → I have **never** encountered this error.

**Note**: "Does not support" is almost always `不支持`. When reporting bugs: "I encountered" = `遇到`, "I did not encounter" = `没遇到`.

---

## 3. `可以 / 能` — capability/permission

**Meaning**: `可以` = permission/option, `能` = ability/physical possibility. In tech docs, often interchangeable.

**Examples**
- 你**可以**通过 API 调用该模型。
  → You **can** call this model through the API.
- 该模型**能**处理长达 128K 的上下文。
  → This model **can** handle context up to 128K.
- 用户**可以**自定义推理参数。
  → Users **can** customize inference parameters.

**Note**: The standard translation of "can". README Features sections use this constantly.

---

## 4. `如果...就` — conditional (if ~ then)

**Meaning**: If/then. `就` can be replaced by `那么` (more emphatic) or `则` (formal/literary).

**Examples**
- **如果**显存不足，**就**减小 batch size。
  → **If** GPU memory is insufficient, reduce batch size.
- **如果**模型加载失败，**则**检查权重文件路径。
  → **If** model loading fails, check the weight file path.
- **如果**遇到 CUDA 错误，**那么**请提交 issue。
  → **If** you encounter a CUDA error, please file an issue.

**Note**: Seeing `则` signals formal/documentation tone. READMEs use `就`, papers and official docs use `则`.

---

## 5. `通过` — by means of / through

**Meaning**: Method or path. Maps to English "via", "through", "by".

**Examples**
- **通过** Docker 部署模型服务。
  → Deploy the model service **via** Docker.
- **通过**调用 generate() 方法生成文本。
  → Generate text **by** calling the `generate()` method.
- 该指标**通过**人工评估得出。
  → This metric is derived **through** human evaluation.

**Note**: `通过 + noun/verb phrase + verb`. Always positioned before the main verb.

---

## 6. `需要` — to require / need

**Meaning**: Necessity. Core verb in System Requirements sections.

**Examples**
- 推理至少**需要** 16GB 显存。
  → Inference **requires** at least 16GB of VRAM.
- 训练**需要**大量标注数据。
  → Training **requires** large amounts of labeled data.
- 您**需要**先安装 CUDA 12.1。
  → You **need** to install CUDA 12.1 first.

**Note**: Appears in nearly every line of a System Requirements section.

---

## 7. `支持 / 不支持` — support / not support

**Meaning**: Whether a feature is supported. The core verb of any tech README.

**Examples**
- 本框架**支持**主流的深度学习模型。
  → This framework **supports** mainstream deep learning models.
- 当前版本**不支持**多 GPU 训练，将在 v2.0 中支持。
  → The current version does **not support** multi-GPU training; this will be supported in v2.0.
- 该模型**支持**中英双语。
  → The model **supports** both Chinese and English.

**Note**: Noun follows directly after `支持`. "Will support soon" = `即将支持`. "Already supports" = `已支持`.

---

## 8. `把` — disposal construction (to do something to X)

**Meaning**: Pulls the object before the verb to emphasize "what was done to it". Frequently used in code-behavior descriptions.

**Examples**
- 请**把**模型转换为 ONNX 格式。
  → Please convert **the** model to ONNX format.
- 系统**把**输入数据切分成多个批次。
  → The system splits **the** input data into multiple batches.
- 我们**把**训练过程分为三个阶段。
  → We divide **the** training process into three phases.

**Note**: Structure: `把 + object + verb + result`. "Convert/split/transform X into Y" patterns nearly always use `把`.

---

## 9. `将` — formal counterpart of `把` (also future tense)

**Meaning**: Same as `把` but more formal. Tech docs and papers prefer `将`. Also marks future tense ("will").

**Examples**
- **将**输入张量传递给模型。
  → Pass the input tensor to the model.
- 我们**将**该方法与基线模型进行比较。
  → We compare this method with the baseline model.
- 下一版本**将**支持流式输出。
  → The next version **will** support streaming output.

**Note**: `将` in a doc = formal tone, `把` = casual. The two meanings (disposal vs. future) are distinguished by context.

---

## 10. `被` — passive voice

**Meaning**: To be ~ed. Common in error messages and behavior descriptions.

**Examples**
- 该参数**被**忽略。
  → This parameter **is** ignored.
- 模型**被**自动加载到 GPU。
  → The model **is** automatically loaded onto the GPU.
- 异常**被**捕获并记录到日志。
  → The exception **is** caught and logged.

**Note**: Mirrors English passive voice. The agent after `被` is optional.

---

## 11. `用于` — used for

**Meaning**: Purpose statement. Standard in model cards and paper abstracts.

**Examples**
- 该模型**用于**自然语言处理任务。
  → This model **is used for** natural language processing tasks.
- 此参数**用于**控制生成长度。
  → This parameter **is used to** control generation length.
- 这些数据**用于**评估模型性能。
  → This data **is used for** evaluating model performance.

**Note**: `用于 + purpose/target`. The opening sentence of nearly every model card.

---

## 12. `基于` — based on

**Meaning**: Foundation, basis. Almost guaranteed to appear in the first paragraph of any README.

**Examples**
- 本模型**基于** Transformer 架构。
  → This model **is based on** the Transformer architecture.
- 我们**基于**开源数据集进行训练。
  → We trained **based on** open-source datasets.
- 这是一个**基于** RAG 的问答系统。
  → This is a RAG-**based** Q&A system.

**Note**: Direct mapping to English "based on". Also used as a noun modifier (`基于 X 的 Y` = "X-based Y").

---

## 13. `对...进行` — perform ~ on / with respect to

**Meaning**: Academic/formal pattern: "perform Y on X". The heavyweight version of a simple verb.

**Examples**
- **对**数据**进行**预处理。
  → Perform preprocessing **on** the data.
- **对**模型**进行**微调。
  → Fine-tune the model. (lit. perform fine-tuning **on** the model)
- **对**实验结果**进行**统计分析。
  → Perform statistical analysis **on** the experimental results.

**Note**: A simple verb stretched out into `对 + noun + 进行 + action-noun`. Used for formal tone in papers. **Without this pattern, you can't read half of any abstract.**

---

## 14. `以...方式` / `以...为` — in ~ manner / take ~ as ~

**Meaning**: Manner, means, or qualification. Frequent formal expression in tech writing.

**Examples**
- **以**异步**方式**执行任务。
  → Execute tasks **in** an asynchronous **manner**.
- **以** JSON 格式返回结果。
  → Return results **in** JSON format.
- **以**准确率**为**主要评估指标。
  → **Take** accuracy **as** the primary evaluation metric.

**Note**: `以 X 方式` = "in X manner" / `以 X 为 Y` = "treat X as Y". The latter is academic.

---

## 15. `得` — degree/result complement

**Meaning**: Attached after a verb to describe how that action is performed. Critical in performance comparisons.

**Examples**
- 该模型训练**得**很快。
  → This model trains **very fast**.
- 推理速度提升**得**非常明显。
  → Inference speed improved **very noticeably**.
- 这个方法效果**得**到了显著改善。
  → This method's effectiveness **was** significantly improved. (※ `得到` = "obtain", a separate word)

**Note**: Two confusion points:
- (a) `verb + 得 + intensifier + adjective`: "how well/fast V is done" (e.g., `跑得快` = "runs fast")
- (b) `得到`: a distinct word meaning "to obtain/receive".
Once you can distinguish these two, you're done.

---

## Bonus 4 — formal patterns to know before Month 2

### `所` + verb — formal passive nominalization

- **所**支持的格式 → "the supported formats"
- **所**采用的方法 → "the adopted method"
- 模型**所**学到的特征 → "the features the model learned"

→ Essentially required for forming noun phrases in papers.

### `即` — that is, namely

- 这是一种零样本学习，**即**不需要任何训练样本。
  → This is a form of zero-shot learning, **i.e.**, requires no training samples.

→ Definition or restatement marker. Equivalent to English "i.e.".

### `如` — for example / such as

- 主流框架**如** PyTorch、TensorFlow。
  → Mainstream frameworks **such as** PyTorch, TensorFlow.

→ Equivalent to English "such as" / "e.g.".

### `亦 / 也` — also

- 该方法**也**适用于多模态场景。
  → This method **also** applies to multimodal scenarios.

→ `亦` is literary, `也` is general. Same meaning.

---

## How to use this document

1. **Make 1 Anki card per pattern** (front: Chinese sentence, back: English + learning note).
2. **Mark each pattern ✓** when you encounter it in real DeepSeek/Qwen READMEs.
3. **Review at end of Month 2** — by then, every example here should read naturally.
