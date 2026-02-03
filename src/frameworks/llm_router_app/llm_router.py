import os
import streamlit as st
from routellm.controller import Controller

# 设置API密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
os.environ["TOGETHERAI_API_KEY"] = "your_togetherai_api_key"

# 初始化RouteLLM客户端
client = Controller(
    routers=["mf"],
    strong_model="gpt-4o-mini",
    weak_model="together_ai/meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
)

st.title("RouteLLM 聊天应用")

# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 展示聊天记录
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "model" in msg:
            st.caption(f"使用模型：{msg['model']}")

# 输入消息
if user_input := st.chat_input("请输入消息："):
    # 记录用户消息
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 获取并展示AI回复
    with st.chat_message("assistant"):
        placeholder = st.empty()
        resp = client.chat.completions.create(
            model="router-mf-0.11593",
            messages=[{"role": "user", "content": user_input}]
        )
        content = resp['choices'][0]['message']['content']
        model_used = resp['model']
        placeholder.markdown(content)
        st.caption(f"使用模型：{model_used}")

    # 记录AI回复
    st.session_state["messages"].append({"role": "assistant", "content": content, "model": model_used})
