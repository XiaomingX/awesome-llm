import streamlit as st
from litellm import completion

st.title("Multi-LLM Chat Playground")

# 输入API Key
api_keys = {
    "gpt": st.text_input("Enter your OpenAI API Key:", type="password"),
    "claude": st.text_input("Enter your Anthropic API Key:", type="password"),
    "cohere": st.text_input("Enter your Cohere API Key:", type="password"),
}

models = {
    "gpt": {"model": "gpt-4o", "name": "GPT-4o", "api_key": api_keys["gpt"]},
    "claude": {"model": "claude-3-5-sonnet-20240620", "name": "Claude 3.5 Sonnet", "api_key": api_keys["claude"]},
    "cohere": {"model": "command-r-plus", "name": "Cohere", "api_key": api_keys["cohere"]},
}

def get_response(model_info, messages):
    try:
        resp = completion(model=model_info["model"], messages=messages, api_key=model_info["api_key"])
        return resp.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if all(api_keys.values()):
    user_input = st.text_input("Enter your message:")
    if st.button("Send to All LLMs"):
        if user_input:
            messages = [{"role": "user", "content": user_input}]
            cols = st.columns(3)
            for col, key in zip(cols, models):
                with col:
                    st.subheader(models[key]["name"])
                    response = get_response(models[key], messages)
                    if response.startswith("Error:"):
                        st.error(response)
                    else:
                        st.write(response)
            st.subheader("Response Comparison")
            st.write("You can see how the three models responded differently to the same input.")
            st.write("This demonstrates the ability to use multiple LLMs in a single application.")
        else:
            st.warning("Please enter a message.")
else:
    st.warning("Please enter all API keys to use the chat.")

# 侧边栏信息
st.sidebar.title("About this app")
st.sidebar.write(
    "This app demonstrates the use of multiple Language Models (LLMs) "
    "in a single application using the LiteLLM library."
)
st.sidebar.subheader("Key features:")
st.sidebar.markdown(
    """
    - Utilizes three different LLMs:
        - OpenAI's GPT-4o
        - Anthropic's Claude 3.5 Sonnet
        - Cohere's Command R Plus
    - Sends the same user input to all models
    - Displays responses side-by-side for easy comparison
    - Showcases the ability to use multiple LLMs in one application
    """
)
st.sidebar.write("Try it out to see how different AI models respond to the same prompt!")
