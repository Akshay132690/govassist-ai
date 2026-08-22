from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def ask_question(query):

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an AI assistant for Indian government schemes.

    Answer ONLY using the context below.

    If answer is not available, say:
    "I could not find this information in the documents."

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content