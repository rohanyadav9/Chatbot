import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

def load_docs_from_folder(folder_path):
    all_docs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            all_docs.extend(docs)
        else:
            print(f"Skipping unsupported file: {filename}")
    return all_docs

def build_faiss_index_from_folder(folder_path):
    print(f"Loading documents from {folder_path}...")
    docs = load_docs_from_folder(folder_path)

    print("Splitting documents into chunks...")
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    print(f"Number of document chunks: {len(split_docs)}")

    print("Creating embeddings...")
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    print("Building FAISS index...")
    db = FAISS.from_documents(split_docs, embedding)

    save_path = "vectorstore/faiss_index"
    os.makedirs(save_path, exist_ok=True)
    db.save_local(save_path)
    print(f"FAISS index saved at {save_path}")

if __name__ == "__main__":
    data_folder = "C:/Users/Rohan yadav/Downloads/Python Documentation"
    build_faiss_index_from_folder(data_folder)
