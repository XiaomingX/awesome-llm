# Awesome LLM (大型语言模型)

🔥 大型语言模型（LLM）持续引领全球 AI 浪潮，已从通用的对话模型进化为具备深度推理（Reasoning）和自主行动（Agentic）能力的智能体。这里整理了关于大型语言模型，特别是与 ChatGPT、Claude、DeepSeek 及 Llama 系列相关的研究论文，涵盖了 LLM 训练框架、部署工具、课程与教程，以及所有公开的 SOTA 模型检查点和 API。

## 热门 LLM 项目

* **[DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)** - 开源界的推理模型里程碑，通过强化学习激发了类似 OpenAI o1 的深度思考能力。
* **[OpenAI o1/o3](https://openai.com/o1)** - 开启了“系统2”思维时代，通过思维链（CoT）在复杂数学、编程和科学问题上实现了突破性表现。
* **[Llama 4 / 3.3](https://llama.meta.com/)** - Meta 继续引领开源，最新的 Llama 4 系列在多模态理解和长上下文处理上设立了新标准。

* **[Ollama](https://github.com/ollama/ollama)** - 目前最流行的本地 LLM 运行工具，支持一键运行 Llama 3.3, Gemma 2, Mistral 等模型。

## 重要论文里程碑

| 日期 | 关键词 | 机构 | 论文 |
| --- | --- | --- | --- |
| 2017-06 | Transformers | Google | [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) |
| 2018-06 | GPT 1.0 | OpenAI | [Improving Language Understanding by Generative Pre-Training](https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf) |
| 2018-10 | BERT | Google | [BERT: Pre-training of Deep Bidirectional Transformers...](https://aclanthology.org/N19-1423.pdf) |
| 2019-02 | GPT 2.0 | OpenAI | [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| 2020-05 | GPT 3.0 | OpenAI | [Language models are few-shot learners](https://papers.nips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf) |
| 2022-01 | COT | Google | [Chain-of-Thought Prompting Elicits Reasoning in LLMs](https://arxiv.org/pdf/2201.11903.pdf) |
| 2022-11 | ChatGPT | OpenAI | [Introducing ChatGPT](https://openai.com/blog/chatgpt) |
| 2023-02 | LLaMA | Meta | [LLaMA: Open and Efficient Foundation Language Models](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) |
| 2023-03 | GPT-4 | OpenAI | [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) |
| 2023-12 | Mamba | CMU/Princeton | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/pdf/2312.00752) |
| 2024-01 | DeepSeek-MoE | DeepSeek | [DeepSeekMoE: Towards Ultimate Expert Specialization...](https://arxiv.org/abs/2401.06066) |
| 2024-05 | Mamba2 | CMU/Princeton | [Transformers are SSMs: Generalized Models...](https://arxiv.org/abs/2405.21060) |
| 2024-06 | Claude 3.5 | Anthropic | [Claude 3.5 Sonnet System Card](https://www.anthropic.com/research) |
| 2024-07 | Llama 3.1 | Meta | [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) |
| 2024-09 | OpenAI o1 | OpenAI | [Learning to Reason with LLMs (System Card)](https://openai.com/index/learning-to-reason-with-llms/) |
| 2024-09 | Qwen 2.5 | Alibaba | [Qwen2.5 Technical Report](https://qwenlm.github.io/blog/qwen2.5/) |
| 2024-12 | DeepSeek-V3 | DeepSeek | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) |
| 2025-01 | DeepSeek-R1 | DeepSeek | [DeepSeek-R1: Incentivizing Reasoning via Reinforcement Learning](https://github.com/deepseek-ai/DeepSeek-R1) |
| 2025-05 | Claude 4 | Anthropic | [Claude 4 Opus Technical Report](https://www.anthropic.com/research) |
| 2025-08 | GPT-5 | OpenAI | [GPT-5 System Card](https://openai.com/gpt-5) |
| 2025-09 | Claude 4.5 | Anthropic | [Claude 4.5 Sonnet Update](https://www.anthropic.com/news) |

## 其他相关论文



* **[LLM推理与思维链 (Reasoning & CoT)](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers)** - 关注 OpenAI o1 和 DeepSeek-R1 引发的推理能力研究。
* **[高效微调与量化](https://github.com/unslothai/unsloth)** - Unsloth, QLoRA 等让个人显卡也能微调大模型的技术。
* **[Agentic Workflow (智能体工作流)](https://github.com/langchain-ai/langgraph)** - 从单一 Prompt 到复杂的智能体协作系统。

## 大型语言模型（LLM）排行榜

* **Chatbot Arena (LMSYS)** - [排行榜链接](https://www.google.com/search?q=https://chat.lmsys.org/) - 业内最权威的盲测排行榜，涵盖 GPT-5, Claude 4.5, Llama 4 等最新模型。
* **OpenCompass 2.0** - [OpenCompass](https://rank.opencompass.org.cn) - 涵盖代码、数学、推理等维度的全方位评测。
* **LiveBench** - [LiveBench](https://livebench.ai/) - 旨在防止“刷榜”的动态基准测试，题目定期更新，更能反映模型真实能力。
* **Open LLM Leaderboard** - [Hugging Face](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) - 针对开源模型的权威自动化评测。

### 开源大语言模型 (LLM)

#### Meta

* **[Llama 4 系列](https://llama.meta.com/)** - 最新的多模态开源王者 (Scout, Maverick, Behemoth)。
* **[Llama 3.3 / 3.1](https://huggingface.co/meta-llama)** - 依然强大的工业级标准模型 (70B, 405B)。

#### DeepSeek (深度求索)

* **[DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)** - 开源推理模型首选，数学与代码能力媲美闭源 SOTA。
* **[DeepSeek-V3](https://huggingface.co/deepseek-ai)** - 极具性价比的 MoE 模型，性能对标 GPT-4o。

#### Alibaba (阿里云)

* **[Qwen 3 (通义千问)](https://github.com/QwenLM/Qwen)** - Qwen 3 系列在编码和数学领域持续霸榜。
* **[Qwen 2.5](https://huggingface.co/Qwen)** - 覆盖 0.5B 到 72B 的全尺寸高性能模型。

#### Mistral AI

* **[Mistral Large 2](https://mistral.ai/)** - 欧洲最强开源模型，上下文窗口大，指令遵循能力强。
* **[Mistral Nemo / Small](https://huggingface.co/mistralai)** - 针对端侧和低延迟场景优化。

#### Google

* **[Gemma 3 / 2](https://ai.google.dev/gemma)** - Google 的轻量级开源模型，适合学术研究和笔记本部署。

#### 其他优秀模型

* **[Phi-4](https://huggingface.co/microsoft)** - Microsoft 推出的“小而美”模型，推理能力惊人。
* **[Nemotron-4](https://huggingface.co/nvidia)** - NVIDIA 发布的用于生成合成数据的重型模型。

### LLM 评估与数据

* **[LiveBench](https://livebench.ai/)** - 防止数据泄露的动态评测。
* **[Scale AI Leaderboard](https://scale.com/leaderboard)** - 专注于代码生成和指令遵循的评测。

## LLM训练框架

* **[Unsloth](https://github.com/unslothai/unsloth)** - **强烈推荐**。训练速度提升 2-5 倍，显存占用减少 50%，是目前微调 Llama/Mistral 的首选工具。
* **[Axolotl](https://www.google.com/search?q=https://github.com/OpenAccess-AI-Collective/axolotl)** - 配置化微调工具，支持绝大多数主流开源模型。
* **[Llama-Factory](https://github.com/hiyouga/LLaMA-Factory)** - 提供 WebUI 的微调框架，对中文用户非常友好。
* **[DeepSpeed](https://github.com/microsoft/DeepSpeed)** & **[Megatron-LM](https://github.com/NVIDIA/Megatron-LM)** - 依然是超大规模集群预训练的基石。

## LLM部署与本地运行

* **[Ollama](https://github.com/ollama/ollama)** - **新手首选**。一个命令即可在 Mac/Linux/Windows 上运行 Llama 3, DeepSeek 等模型。
* **[vLLM](https://github.com/vllm-project/vllm)** - 生产环境的首选推理引擎，支持 PagedAttention，吞吐量极高。
* **[LM Studio](https://lmstudio.ai/)** - 带有图形界面的本地模型运行工具，支持 GGUF 格式。
* **[SGLang](https://github.com/sgl-project/sglang)** - 针对复杂 Prompt 流程优化的推理框架，速度比 vLLM 更快。
* **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)** - NVIDIA 官方推出的极致优化推理库。
* **[Open WebUI](https://github.com/open-webui/open-webui)** - **强烈推荐**。功能最强大的本地 LLM Web 界面，完美支持 Ollama 和 OpenAI API。
* **[LiteLLM](https://github.com/BerriAI/litellm)** - 用 OpenAI 格式调用 100+ 种 LLM API (Anthropic, Vertex, Ollama 等)。

## LLM 编程助手 (AI Coding Assistants)

* **[Cursor](https://www.cursor.com/)** - **当前体验最佳**。基于 VS Code 修改的 AI 原生编辑器，Tab 补全和 Composer 功能极大地改变了编程体验。
* **[Windsurf](https://codeium.com/windsurf)** - Codeium 推出的 Agentic IDE，主打深度上下文感知和主动行动能力。
* **[Cline](https://github.com/cline/cline)** - 开源的自主编程 Agent 插件，能够执行终端命令、文件读写，配合 Claude 3.5 Sonnet 效果拔群。
* **[Continue](https://github.com/continuedev/continue)** - 开源的 IDE 插件 (VS Code / JetBrains)，支持连接本地 Ollama 模型进行辅助编程。

## LLM应用与智能体 (Agent)

* **[LangGraph](https://github.com/langchain-ai/langgraph)** - LangChain 的升级版，专注于构建有状态、循环的智能体工作流。
* **[Dify](https://github.com/langgenius/dify)** - 开源的 LLM 应用开发平台，可视化编排 RAG 和 Agent。
* **[MemGPT](https://github.com/cpacker/MemGPT)** - 赋予 LLM 长期记忆和操作系统级别的上下文管理能力。
* **[CrewAI](https://github.com/joaomdmoura/crewAI)** - 编排角色扮演的 AI 智能体团队来共同完成任务。
## 提示工程与优化 (Prompt Engineering)

* **[DSPy](https://github.com/stanfordnlp/dspy)** - 斯坦福推出的框架，主张“编程”而非“提示”语言模型，通过编译自动优化 Prompt。
* **[Promptfoo](https://github.com/promptfoo/promptfoo)** - 开发者友好的 LLM 测试工具，用于评估 Prompt 质量和模型输出，防止回归。

## LLM教程与课程 (2025版)

* **[Andrej Karpathy's LLM101n](https://github.com/karpathy/LLM101n)** - Karpathy 大神的最新课程，教你从零构建一个 Storyteller AI。
* **[Generative AI with LLMs (Coursera)](https://www.coursera.org/learn/generative-ai-with-llms)** - AWS 和 DeepLearning.AI 联合推出的实战课程。
* **[DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)** - 包含 RAG、Agent、Fine-tuning 等大量免费短课程。
