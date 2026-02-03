<p align="center">
<img width="1000px" alt="Awesome DeepSeek Coder" src="images/Awesome_DeepSeek_Coder.png">
</p>

📚 [English](https://github.com/deepseek-ai/awesome-deepseek-coder/blob/main/README.md) | [中文]
<br> 

# awesome-deepseek-coder ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

与 DeepSeek Coder 相关的资源&开源项目的精选列表
<br> <br>

## 快速体验 DeepSeek Coder
👉直达官网内测页面  [chat.deepseek.com](https://chat.deepseek.com/)
<br> <br>
## 官方资源
### 已发布的模型
所有模型均可在 Hugging Face 官方主页（@deepseek_ai）进行下载
<br>🔗[huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai)<br>

| Model Size | Base | Instruct |
|------------|------|----------|
| **1.3B**        | [deepseek-coder-1.3b-base](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base) | [deepseek-coder-1.3b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct) |
| **5.7B**     | [deepseek-coder-5.7bmqa-base](https://huggingface.co/deepseek-ai/deepseek-coder-5.7bmqa-base) | [deepseek-coder-5.7bmqa-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-5.7bmqa-instruct)(coming soon) |
| **6.7B**       | [deepseek-coder-6.7B-base](https://huggingface.co/deepseek-ai/deepseek-coder-6.7B-base) | [deepseek-coder-6.7B-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7B-instruct) |
| **33B**         | [deepseek-coder-33B-base](https://huggingface.co/deepseek-ai/deepseek-coder-33B-base) | [deepseek-coder-33B-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-33B-instruct) |

### API 开放平台
轻松接入，让DeepSeek成为你高效的AI助手
 <br>🔗[platform.deepseek.com](https://platform.deepseek.com/) 
<br> 
## 社区生态资源
### 基于 DeepSeek Coder 训练的模型

| Model Size | Models | 
|------------|------|
| **1.3B**        | [OpenCodeInterpreter-DS-1.3B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-1.3B) |
| **6.7B**       | [Magicoder-DS-6.7B](https://huggingface.co/ise-uiuc/Magicoder-DS-6.7B) <br> [Magicoder-S-DS-6.7B](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B) <br> [OpenCodeInterpreter-DS-6.7B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-6.7B) <br> [openbuddy-deepseekcoder-6b-v16.1-32k](https://huggingface.co/OpenBuddy/openbuddy-deepseekcoder-6b-v16.1-32k) | 
| **33B**         | [WizardCoder-33B-V1.1](https://huggingface.co/WizardLM/WizardCoder-33B-V1.1) <br> [CodeFuse-DeepSeek-33B](https://huggingface.co/codefuse-ai/CodeFuse-DeepSeek-33B) <br> [OpenCodeInterpreter-DS-33B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B) <br> [openbuddy-deepseekcoder-33b-v16.1-32k](https://huggingface.co/OpenBuddy/openbuddy-deepseekcoder-33b-v16.1-32k)| 


### 量化模型 

- [TheBloke](https://huggingface.co/TheBloke) - TheBloke 为 Deepseek Coder 1B/7B/33B 模型开发 AWQ/GGUF/GPTQ 格式模型文件

| Model Size | Base | Instruct |
|------------|------|----------|
| **1.3B**   | [deepseek-coder-1.3b-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-AWQ) <br> [deepseek-coder-1.3b-base-GGUF](https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-GGUF) <br> [deepseek-coder-1.3b-base-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-1.3b-base-GPTQ) | [deepseek-coder-1.3b-instruct-AWQ](https://huggingface.co/TheBloke/deepseek-coder-1.3b-instruct-AWQ) <br> [deepseek-coder-1.3b-instruct-GGUF](https://huggingface.co/TheBloke/deepseek-coder-1.3b-instruct-GGUF) <br> [deepseek-coder-1.3b-instruct-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-1.3b-instruct-GPTQ) |
| **5.7B**   | [deepseek-coder-5.7bmqa-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-base-AWQ) <br> [deepseek-coder-5.7bmqa-base-GGUF](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-base-GGUF) <br> [deepseek-coder-5.7bmqa-base-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-base-GPTQ) | [deepseek-coder-5.7bmqa-instruct-AWQ](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-instruct-AWQ)(coming soon) <br> [deepseek-coder-5.7bmqa-instruct-GGUF](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-instruct-GGUF)(coming soon) <br> [deepseek-coder-5.7bmqa-instruct-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-5.7bmqa-instruct-GPTQ)(coming soon) |
| **6.7B**   | [deepseek-coder-6.7B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-6.7B-base-AWQ) <br> [deepseek-coder-6.7B-base-GGUF](https://huggingface.co/TheBloke/deepseek-coder-6.7B-base-GGUF) <br> [deepseek-coder-6.7B-base-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-6.7B-base-GPTQ) | [deepseek-coder-6.7B-instruct-AWQ](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-AWQ) <br> [deepseek-coder-6.7B-instruct-GGUF](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF) <br> [deepseek-coder-6.7B-instruct-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GPTQ) |
| **33B**    | [deepseek-coder-33B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-33B-base-AWQ) <br> [deepseek-coder-33B-base-GGUF](https://huggingface.co/TheBloke/deepseek-coder-33B-base-GGUF) <br> [deepseek-coder-33B-base-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-33B-base-GPTQ) | [deepseek-coder-33B-instruct-AWQ](https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-AWQ) <br> [deepseek-coder-33B-instruct-GGUF](https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-GGUF) <br> [deepseek-coder-33B-instruct-GPTQ](https://huggingface.co/TheBloke/deepseek-coder-33B-instruct-GPTQ) |

### Copilot
👉 [refact](https://github.com/smallcloudai/refact)  <br>开源人工智能编码助手，具有极快的代码完成速度、强大的代码改进工具和聊天功能。它支持 `deepseek-coder/1.3b/base`, `deepseek-coder/5.7b/mqa-base`, `deepseek-coder/6.7b/instruct`, `deepseek-coder/33b/instruct`.

👉 [Tabby](https://github.com/TabbyML/tabby)<br>开源、自托管的 AI 编码助手，是 GitHub Copilot 的有力替代品。 可以在 Tabby 上深入探索 DeepSeek Coder 强大的代码补全功能✨ [(link)](https://tabby.tabbyml.com/docs/models/)。<br>其最新排行榜显示 deepseek-coder-6.7B 在代码完成方面表现最佳 (https://leaderboard.tabbyml.com/).  
<p align="center">
<img width="500px" alt="Tabby-Leaderboard" src="images/Tabby-Leaderboard.png">
</p>

👉 [🧙‍AutoDev](https://github.com/unit-mesh/auto-dev) <br> 开源的AI辅助编程工具，可以与Jetbrains系列IDE无缝集成。 它提供 Deepseek Coder 6.7B 微调数据工具[Unit Eval](https://github.com/unit-mesh/unit-eval), 与 AutoDev 提示相关的 [datasets](https://huggingface.co/datasets/unit-mesh/unit-eval-completion) 和 [finetuned model](https://huggingface.co/unit-mesh/autodev-deepseek-6.7b-finetunes), 以及 [API server example](https://github.com/unit-mesh/unit-eval/blob/master/finetunes/deepseek/api-server-python38.py)

### APIs
- [limcheekin/deepseek-coder-6.7B-instruct-GGUF](https://huggingface.co/spaces/limcheekin/deepseek-coder-6.7B-instruct-GGUF): limcheekin 为“deepseek-coder-6.7B-instruct-GGUF”模型提供 API

## 创意持续征集中ing
😃感谢各位对 DeepSeek Coder的认可与支持！很高兴看到如此有价值的创作与项目！<br>🙋如果你有新的创作没有被收录，欢迎随时联系我们！
