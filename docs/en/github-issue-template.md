# GitHub Issue Templates in Chinese

> Copy-paste templates for filing Issues, Discussions, or PRs on Chinese open-source projects (DeepSeek, Qwen, GLM, etc.).
> Replace `[bracketed]` placeholders with your situation.

---

## 1. Bug Report

```markdown
## 问题描述

[One-sentence summary of the bug]

## 环境信息

- 操作系统：[e.g., Ubuntu 22.04 / macOS 14.5 / Windows 11]
- Python 版本：[e.g., 3.11.7]
- 框架版本：[e.g., torch 2.3.0, transformers 4.42.0]
- GPU：[e.g., NVIDIA A100 40GB / RTX 4090 / no GPU]
- CUDA 版本：[e.g., 12.1]
- 模型版本：[e.g., DeepSeek-V3-Base]

## 复现步骤

1. [Step 1]
2. [Step 2]
3. [Step 3]

## 预期行为

[What you expected]

## 实际行为

[What actually happened]

## 报错信息

\```
[Full stack trace / error log]
\```

## 已尝试的解决方案

- [Attempt 1]
- [Attempt 2]
- 已查阅相关 issue：#[related issue number]，但未找到解决方案。

## 补充信息

[Screenshots, additional context, suspected cause]
```

---

## 2. Feature Request

```markdown
## 需求背景

[Why this feature is needed, what scenario]

## 期望的功能

[Specific feature requested]

## 替代方案

[Current workaround if any]

## 参考实现

[Links to similar implementations or papers]

## 补充说明

[Additional info]
```

---

## 3. Question / Usage Inquiry

```markdown
## 问题

[One-sentence question]

## 我尝试了什么

[What you've already tried — searched docs, checked code, etc.]

## 具体场景

[Your specific situation — what data, what goal]

## 期望得到的帮助

[What kind of answer you want — code example, conceptual explanation, recommendation]

## 环境信息（如相关）

- Python 版本：
- 框架版本：
- 模型：
```

---

## 4. Performance / OOM Issue

```markdown
## 问题描述

在运行 [model name] 的推理时遇到显存不足（OOM）问题。

## 环境信息

- GPU：[GPU model + VRAM]
- CUDA 版本：
- 框架版本：
- 模型：[model name + parameter count]
- 输入长度：[input token length]
- 批大小：[batch size]

## 报错信息

\```
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate ...
\```

## 已尝试的优化

- [ ] 减小 batch size 至 [number]
- [ ] 启用梯度检查点（gradient checkpointing）
- [ ] 使用混合精度（fp16 / bf16）
- [ ] 启用模型量化（[INT8 / INT4]）
- [ ] 减小最大序列长度
- [ ] 使用 CPU offload

## 期望

请问是否有推荐的配置可以在 [VRAM size]GB 显存上运行该模型？
```

---

## 5. Model Download / Loading Issue

```markdown
## 问题描述

无法成功加载 [model name]。

## 环境信息

- 操作系统：
- Python 版本：
- 网络环境：[e.g., 中国大陆 / 海外 / 公司内网]
- 模型来源：[e.g., HuggingFace / ModelScope / local path]

## 复现代码

\```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("[model path]")
\```

## 报错信息

\```
[Full error message]
\```

## 已尝试的方法

- [ ] 使用镜像源（HF_ENDPOINT=https://hf-mirror.com）
- [ ] 手动下载权重文件
- [ ] 使用 modelscope 替代 huggingface_hub
- [ ] 检查 token 权限
```

---

## 6. Pull Request Description

```markdown
## 变更概述

[One paragraph: what this PR does]

## 关联 Issue

Closes #[issue number]

## 变更类型

- [ ] Bug 修复
- [ ] 新增功能
- [ ] 性能优化
- [ ] 文档更新
- [ ] 代码重构

## 详细变更

- [Change 1]
- [Change 2]
- [Change 3]

## 测试

- [ ] 已添加单元测试
- [ ] 已通过现有测试
- [ ] 已在本地验证：[tested environment]

## 截图 / 性能对比

[If applicable]

## 检查清单

- [ ] 代码符合项目规范
- [ ] 已更新相关文档
- [ ] 提交信息清晰明确
```

---

## 7. Self-Resolved Reply

```markdown
已解决，原因如下：

[Explanation of root cause]

## 解决方案

[Solution]

\```python
# Code example
\```

希望对遇到相同问题的人有帮助。感谢社区的支持，关闭此 issue。
```

---

## 8. Thanks + Follow-up Question

```markdown
感谢您的回复！

按照您的建议，我 [what you tried]，结果 [outcome].

不过还有一个问题：[follow-up question].

请问 [specific question]？
```

---

## Common One-Liners

| English | Chinese |
|---------|---------|
| Hello, I'd like to report an issue | 您好，我想反馈一个问题 |
| I encountered ~ | 我遇到了 ... |
| Reliably reproducible | 可以稳定复现 |
| Cannot reliably reproduce | 无法稳定复现 |
| I tried ~ but it didn't work | 我尝试了 ... 但没有效果 |
| Please help take a look | 请帮忙看看 |
| Thank you for taking the time | 感谢您抽时间查看 |
| Let me know if you need more info | 如需更多信息请告知 |
| Related code is below | 相关代码如下 |
| I'm having the same issue | 我也遇到了同样的问题 |
| +1 (agree) | 同+1 |
| This issue is still unresolved | 这个问题还没解决 |
| I've submitted a PR | 已提交 PR：#[number] |
| Will be fixed in next release | 将在下一版本中修复 |

---

## Tone Guide

- Chinese open-source communities default to formal address (`您`, not `你`).
- Prefer softeners like `请` `麻烦` `感谢` over blunt directives.
- English technical terms can be left in English (PyTorch, transformer, batch size, etc.).
- Code blocks use the same triple-backtick syntax.
- Avoid emojis. Chinese OSS issue trackers are noticeably more restrained than English ones.
