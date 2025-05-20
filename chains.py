from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from prompt_template import prompt_template
from langchain_google_genai import ChatGoogleGenerativeAI  
import streamlit as st


# Load vectorstore
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local(
    "vectorstore/faiss_index",
    embedding,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

# Build main chain
parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",  google_api_key=st.secrets["GOOGLE_API_KEY"])
main_chain = parallel_chain | prompt_template | llm | StrOutputParser()
