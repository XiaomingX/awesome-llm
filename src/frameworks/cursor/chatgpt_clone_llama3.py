import streamlit as st
from ollama import Client

# 初始化 Ollama 客户端
client = Client()

# 设置页面配置
st.set_page_config(page_title="本地ChatGPT克隆", page_icon="🤖", layout="wide")
st.title("🤖 本地ChatGPT克隆")

# 初始化会话消息列表
if "消息列表" not in st.session_state:
    st.session_state.消息列表 = []

# 展示已有的聊天记录
for msg in st.session_state.消息列表:
    with st.chat_message(msg["角色"]):
        st.markdown(msg["内容"])

# 用户输入处理
if 用户输入 := st.chat_input("你有什么想法？"):
    st.session_state.消息列表.append({"角色": "user", "内容": 用户输入})
    with st.chat_message("user"):
        st.markdown(用户输入)

    # AI回复生成并实时展示
    with st.chat_message("assistant"):
        占位符 = st.empty()
        回复内容 = ""
        for 响应 in client.chat(model="llama3.1:latest", messages=st.session_state.消息列表, stream=True):
            回复内容 += 响应['message']['content']
            占位符.markdown(回复内容 + "▌")
        占位符.markdown(回复内容)
    st.session_state.消息列表.append({"角色": "assistant", "内容": 回复内容})

# 侧边栏信息
st.sidebar.title("关于")
st.sidebar.info("本地ChatGPT克隆，基于Ollama的llama3.1:latest模型和Streamlit实现。")
st.sidebar.markdown("---")
st.sidebar.markdown("由 ❤️ Your Name 制作")
