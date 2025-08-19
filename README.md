# Agentic-RAG

Adaptive Agentic RAG with LangGraph – a production-ready Retrieval-Augmented Generation (RAG) pipeline that dynamically routes queries, detects hallucinations, grades answers, and leverages web search when needed.

## ✨ Features
- **Adaptive Routing** – routes questions to vectorstore or web search depending on context.
- **Document Grading** – filters retrieved documents for relevance before generation.
- **Hallucination Detection** – verifies that model responses are grounded in retrieved documents.
- **Answer Grading** – checks whether the generated answer actually addresses the original question.
- **LangGraph Workflow** – each step (retrieve, grade, generate, websearch) is represented as a graph node with conditional edges.
- **Mermaid Graph Export** – visualize the entire workflow (graph.png) for debugging & documentation.
- **Configurable & Extensible** – swap vectorstores, LLMs, or graders with minimal changes.

## 📂 Project Structure
```
adaptive-rag/
├── graph/
│   ├── graph.py            # Defines the LangGraph workflow
│   ├── state.py            # Shared graph state definition
│   ├── nodes/              # Individual nodes (retrieve, generate, grade, websearch)
│   ├── chains/             # LLM chains for grading & routing
├── consts.py           # Node constants
├── ingestion.py            # Builds retriever/vectorstore from documents
├── model.py                # Embedding & model setup
├── main.py                 # Entry point
├── config.py               # Centralized settings/env management
└── README.md               # Project documentation
```

## 🚀 Getting Started
1. Clone the repo
```
git clone https://github.com/<your-username>/adaptive-rag.git
cd adaptive-rag
```
2 Create environment
```
uv venv --python 3.11
uv pip install -r requirements.txt 
```
3. Set up environment variables
```
GOOGLE_API_KEY=YOUR_API_KEY
TAVILY_API_KEY=YOUR_API_KEY  # For web search capabilities
USER_AGENT=adaptive-rag/1.0
```

4. Run
```
uv run python main.py
```

## 🛠 Customization
- **Retriever** – adjust chunk size, overlap, or vector DB in ingestion.py.
- **Models** – swap out embeddings (GoogleGenerativeAIEmbeddings, OpenAIEmbeddings, etc.) in model.py.
- **Graders** – tune hallucination/answer grader prompts in graph/chains/.

