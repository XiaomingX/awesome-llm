import streamlit as st
import google.generativeai as genai
from PIL import Image

# 页面配置
st.set_page_config(page_title="多模态聊天机器人（Gemini Flash）", layout="wide")
st.title("多模态聊天机器人（Gemini Flash ⚡️）")
st.caption("通过图片和文本输入，与谷歌 Gemini Flash 模型对话，体验极速响应。🌟")

# 输入API密钥
api_key = st.text_input("请输入Google API密钥", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

    # 初始化会话消息列表
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 侧边栏上传图片
    with st.sidebar:
        st.title("上传图片聊天")
        uploaded_file = st.file_uploader("选择图片（jpg/jpeg/png）", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="已上传图片", use_column_width=True)

    # 展示聊天记录
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # 用户输入
    prompt = st.chat_input("请输入您的问题")

    if prompt:
        inputs = [prompt]
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)

        if uploaded_file:
            inputs.append(image)

        with st.spinner("正在生成回复..."):
            response = model.generate_content(inputs)

        st.session_state.messages.append({"role": "assistant", "content": response.text})
        with chat_container:
            with st.chat_message("assistant"):
                st.markdown(response.text)

    elif uploaded_file:
        st.warning("请同时输入文本问题，以便结合图片进行回答。")
else:
    st.info("请输入有效的Google API密钥以开始使用。")
