# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a curated collection of LLM applications, tutorials, and resources focused on large language models (LLMs), particularly ChatGPT, Claude, DeepSeek, and Llama series. The repository is primarily a documentation and tutorial collection rather than a single unified codebase.

## Repository Structure

The repository is organized into distinct categories under the `src/` directory:

- **`src/agents/`** - AI agent implementations using frameworks like CrewAI, AutoGen, and multi-agent systems
- **`src/chatbots/`** - Custom chatbot implementations (chat with PDF, GitHub, Gmail, YouTube, etc.)
- **`src/frameworks/`** - Advanced framework examples (Gemini multimodal, LLM routers, web scrapers)
- **`src/rag/`** - Retrieval-Augmented Generation (RAG) systems with various vector databases
- **`src/finetuning/`** - Fine-tuning guides for models like Llama 3.2
- **`src/memory/`** - LLM applications with long-term memory and context management

Each subdirectory is a **standalone project** with its own:
- `README.md` - Setup instructions and feature descriptions
- `requirements.txt` - Python dependencies
- Python scripts (typically named descriptively, e.g., `customer_support_agent.py`)

## Working with Individual Projects

### Running a Project

1. Navigate to the specific project directory:
   ```bash
   cd src/agents/ai_customer_support_agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up required API keys (varies by project):
   ```bash
   export OPENAI_API_KEY='your-key-here'
   ```

4. Run the application (check the project's README for specific commands):
   ```bash
   # For Streamlit apps
   streamlit run customer_support_agent.py

   # For Python scripts
   python3 rag_agent.py
   ```

### Common Dependencies

Most projects use one or more of:
- **OpenAI API** - GPT-4o, GPT-4o-mini models
- **Streamlit** - Web UI framework for many applications
- **Vector Databases** - Qdrant, LanceDB, ChromaDB for RAG systems
- **Memory Libraries** - mem0ai for persistent memory
- **Agent Frameworks** - phi (phidata), CrewAI, LangChain/LangGraph

### External Services

Some projects require running external services:

**Qdrant (Vector Database)**:
```bash
docker pull qdrant/qdrant
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

## Key Architectural Patterns

### RAG Applications
- Use vector databases (LanceDB, Qdrant) for similarity search
- Knowledge bases typically loaded from PDFs or web URLs
- Often include web search tools (DuckDuckGo) for real-time information

### Agent Applications
- Built with frameworks like phi.agent, CrewAI
- Use tool calling for web search, calculations, API access
- Often include playground interfaces for testing

### Memory-Enabled Applications
- Use mem0ai library with vector stores for persistent memory
- Store user interactions and preferences
- Retrieve relevant context for personalized responses

## Important Notes

- **No unified build system** - Each project is independent
- **API keys required** - Most projects need OpenAI or other LLM provider keys
- **Check individual READMEs** - Setup steps vary significantly between projects
- **Python 3.x required** - Most projects use modern Python features
- **Docker may be needed** - For vector databases and other services

## Repository Purpose

This is primarily a **learning and reference repository** containing:
- Tutorial code demonstrating LLM application patterns
- Example implementations of common LLM use cases
- Documentation of LLM tools, frameworks, and models
- Curated lists of papers, models, and resources in the main README.md

When modifying this repository, focus on:
- Keeping individual projects self-contained
- Maintaining clear README documentation for each project
- Ensuring requirements.txt files are accurate
- Following the established directory structure
