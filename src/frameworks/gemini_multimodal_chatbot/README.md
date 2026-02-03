## ⚡️ 多模态聊天机器人（基于 Gemini Flash）

本项目展示了一个基于 Google Gemini Flash 模型的多模态聊天机器人，支持图片和文本输入，响应速度极快。

### 主要功能
- **多模态输入**：支持上传图片和文本提问。
- **Gemini Flash 模型**：采用谷歌轻量级但高效的 Gemini Flash 模型。
- **聊天记录**：自动保存并展示对话历史。

### 快速开始

1. 克隆代码库：

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 获取 Google AI Studio API Key：

- 访问 [Google AI Studio](https://aistudio.google.com/app/apikey) 注册并申请 API Key。

4. 启动应用：

```bash
streamlit run gemini_multimodal_chatbot.py
```