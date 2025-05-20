from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""
)
