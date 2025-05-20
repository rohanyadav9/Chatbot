📚 Your Own Python Tutor....
An AI-powered assistant that answers your questions about Python using context-aware responses from official Python documentation. It uses Google Gemini, LangChain, and FAISS to create a local vector-based semantic search over Python docs.

🚀 Features
Ask questions in natural language about Python

Semantic search using FAISS for accurate context

Gemini model generates high-quality answers

Streamlit-based sleek UI

Option to export Q&A conversation as PDF

Local vector database – no external API for doc retrieval

Clean, extendable modular code (LangChain Runnables)


🧠 Tech Stack
Python

Streamlit – for UI

Google Gemini (via langchain-google-genai)

LangChain – for chaining and retrieval pipeline

FAISS – for fast vector similarity search

Sentence Transformers – for embeddings

PyMuPDF / PDFMiner – for PDF parsing (optional)

ReportLab / FPDF – for saving conversations as PDF

📁 Folder Structure
.
├── app.py                      # Streamlit frontend
├── build_data.py              # Build FAISS vectorstore from docs
├── chains.py                  # LangChain chains: retrieval + LLM
├── prompt_template.py         # Prompt template for Gemini
├── requirements.txt
├── vectorstore/               # FAISS index and pickle file
└── .gitignore



