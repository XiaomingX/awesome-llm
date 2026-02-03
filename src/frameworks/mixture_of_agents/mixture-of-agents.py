import streamlit as st
import asyncio
import os
from together import AsyncTogether, Together

st.title("Mixture-of-Agents LLM App")

def get_api_key():
    return st.text_input("Enter your Together API Key:", type="password")

def get_user_prompt():
    return st.text_input("Enter your question:")

def create_clients(api_key):
    os.environ["TOGETHER_API_KEY"] = api_key
    return Together(api_key=api_key), AsyncTogether(api_key=api_key)

reference_models = [
    "Qwen/Qwen2-72B-Instruct",
    "Qwen/Qwen1.5-72B-Chat",
    "mistralai/Mixtral-8x22B-Instruct-v0.1",
    "databricks/dbrx-instruct",
]
aggregator_model = "mistralai/Mixtral-8x22B-Instruct-v0.1"

aggregator_system_prompt = (
    "You have been provided with a set of responses from various open-source models to the latest user query. "
    "Your task is to synthesize these responses into a single, high-quality response. "
    "It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. "
    "Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. "
    "Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability. Responses from models:"
)

async def run_llm(async_client, model, prompt):
    resp = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    return model, resp.choices[0].message.content

async def main(async_client, client, prompt):
    results = await asyncio.gather(*[run_llm(async_client, m, prompt) for m in reference_models])

    st.subheader("Individual Model Responses:")
    for model, response in results:
        with st.expander(f"Response from {model}"):
            st.write(response)

    st.subheader("Aggregated Response:")
    stream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {"role": "system", "content": aggregator_system_prompt},
            {"role": "user", "content": ",".join(r for _, r in results)},
        ],
        stream=True,
    )

    container = st.empty()
    full_resp = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        full_resp += content
        container.markdown(full_resp + "▌")
    container.markdown(full_resp)

api_key = get_api_key()
if api_key:
    client, async_client = create_clients(api_key)
    user_prompt = get_user_prompt()
    if st.button("Get Answer"):
        if user_prompt:
            asyncio.run(main(async_client, client, user_prompt))
        else:
            st.warning("Please enter a question.")
else:
    st.warning("Please enter your Together API key to use the app.")

st.sidebar.title("About this app")
st.sidebar.write(
    "This app demonstrates a Mixture-of-Agents approach using multiple Language Models (LLMs) "
    "to answer a single question."
)
st.sidebar.subheader("How it works:")
st.sidebar.markdown(
    """
    1. The app sends your question to multiple LLMs:
        - Qwen/Qwen2-72B-Instruct
        - Qwen/Qwen1.5-72B-Chat
        - mistralai/Mixtral-8x22B-Instruct-v0.1
        - databricks/dbrx-instruct
    2. Each model provides its own response
    3. All responses are then aggregated using Mixtral-8x22B-Instruct-v0.1
    4. The final aggregated response is displayed
    """
)
st.sidebar.write(
    "This approach allows for a more comprehensive and balanced answer by leveraging multiple AI models."
)
