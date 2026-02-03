import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

st.title("AI网页智能爬取器")

# 用户输入
信息需求 = st.text_input("请输入您想提取的信息内容：")
网址 = st.text_input("请输入网页链接：")
密钥 = st.text_input("请输入OpenAI API密钥：", type="password")

配置 = {
    "llm": {"api_key": 密钥, "model": "openai/gpt-4o-mini"},
    "verbose": True,
    "headless": False,
}

if st.button("开始爬取"):
    if 信息需求 and 网址 and 密钥:
        爬虫 = SmartScraperGraph(prompt=信息需求, source=网址, config=配置)
        结果 = 爬虫.run()
        st.write(结果)
    else:
        st.error("请完整填写所有输入项！")

st.markdown("""
### 使用说明
1. 输入您想提取的信息内容。
2. 输入目标网页链接。
3. 输入您的OpenAI API密钥。
4. 点击“开始爬取”按钮，等待结果显示。
""")
