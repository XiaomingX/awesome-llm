## 📡 RouteLLM 聊天应用简介

> 本项目基于开源的 [RouteLLM](https://github.com/lm-sys/RouteLLM/tree/main) 库，支持根据任务复杂度智能选择不同的语言模型，实现高效问答路由。

### 功能亮点

- 聊天界面，方便与AI模型互动  
- 自动选择最适合的模型（GPT-4 mini 和 Meta-Llama 3.1 70B Turbo）  
- 显示聊天记录及对应模型信息  

### 快速开始

1. 克隆代码仓库：

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

3. 配置API密钥（建议使用环境变量）：

```python
import os
os.environ["OPENAI_API_KEY"] = "你的OpenAI密钥"
os.environ["TOGETHERAI_API_KEY"] = "你的TogetherAI密钥"
```

4. 启动应用：

```bash
streamlit run llm_router.py
```

### 工作原理简述

- 初始化RouteLLM控制器，载入强模型（GPT-4 mini）和弱模型（Meta-Llama 3.1）  
- 用户通过聊天界面输入问题  
- RouteLLM根据问题复杂度自动选择合适模型  
- 选中模型生成回答  
- 显示回答及使用的模型信息  
- 保留并展示完整聊天历史  

---

此版本去掉了重复和过于详细的说明，语言更符合中文习惯，结构清晰，方便中国开发者快速理解和上手[2][3][4]。如果需要在代码中添加中文注释，也建议用简洁明了的句子说明变量、函数功能，保证UTF-8编码，方便团队协作和后期维护[3][5]。

Citations:
[1] https://github.com/lm-sys/RouteLLM/tree/main
[2] https://www.minjiekaifa.com/agilearticles/code-comment-guide-80497.mhtml
[3] https://docs.pingcode.com/ask/262360.html
[4] https://www.cnblogs.com/guoxiaoyu/p/18313588
[5] https://docs.pingcode.com/baike/278160
[6] https://www.cnblogs.com/bdqczhl/p/5786977.html
[7] https://blog.csdn.net/llf021421/article/details/8214232
[8] https://blog.csdn.net/zhoushimiao1990/article/details/122686402
[9] https://blog.csdn.net/ruanrunxue/article/details/103449587
[10] https://zh-style-guide.readthedocs.io/zh-cn/latest/%E6%96%87%E6%A1%A3%E5%86%85%E5%AE%B9%E5%85%83%E7%B4%A0/%E4%BB%A3%E7%A0%81%E5%9D%97%E5%92%8C%E4%BB%A3%E7%A0%81%E6%B3%A8%E9%87%8A.html
[11] https://tech.meituan.com/2017/01/19/clean-code.html

---
来自 Perplexity 的回答: pplx.ai/share