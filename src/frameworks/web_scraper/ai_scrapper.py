import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

def main():
    st.title("Web Scraping AI Agent 🕵️‍♂️")
    st.caption("This app allows you to scrape a website using OpenAI API")

    api_key = st.text_input("OpenAI API Key", type="password")
    if not api_key:
        return

    model = st.radio("Select the model", ["gpt-3.5-turbo", "gpt-4"])
    url = st.text_input("Enter the URL of the website you want to scrape")
    prompt = st.text_input("What do you want the AI agent to scrape from the website?")

    if st.button("Scrape") and url and prompt:
        config = {"llm": {"api_key": api_key, "model": model}}
        scraper = SmartScraperGraph(prompt=prompt, source=url, config=config)
        result = scraper.run()
        st.write(result)

if __name__ == "__main__":
    main()
