# 🇮🇳 GovAssist AI                     [![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://govassist-ai.streamlit.app/)

GovAssist AI is an AI-powered Government Scheme Recommendation System that helps users discover relevant government schemes and get answers to their queries using Retrieval-Augmented Generation (RAG).



<p align="center">
  <img src="/home.png" width="900">
</p>


<p align="center">
  <img src="/askAI.png" width="900">
</p>


## 🚀 Features

- 🔍 Eligibility-based government scheme recommendations
- 💬 AI-powered question answering
- 📄 Multi-document PDF knowledge base
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Semantic search using FAISS
- 🤖 Google Gemini integration
- 🌐 Streamlit web application
- ☁️ Deployed on Streamlit Cloud

---

## 🏗️ System Architecture

```text
Government Scheme PDFs
          ↓
     Text Chunking
          ↓
      Embeddings
          ↓
     FAISS Vector DB
          ↓
      Retriever
          ↓
      Gemini API
          ↓
    Generated Answer
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & NLP
- LangChain
- Google Gemini API
- Sentence Transformers

### Vector Database
- FAISS

### Document Processing
- PyPDF

---

## 📋 Project Workflow

1. Government scheme PDFs are loaded.
2. Documents are split into smaller chunks.
3. Embeddings are generated using Sentence Transformers.
4. Embeddings are stored in FAISS.
5. User submits a query.
6. Relevant chunks are retrieved using semantic search.
7. Retrieved context is sent to Gemini.
8. Gemini generates a context-aware response.

---

## 🎯 Eligibility Recommendation Module

Users provide:
- Age
- Occupation
- Annual Income

The system:
- Checks eligibility rules
- Recommends matching schemes
- Provides AI-generated explanations

---

## 📂 Project Structure

```text
govassist-ai/
│
├── app.py
├── rag_pipeline.py
├── eligibility.py
├── ingest.py
├── schemes.json
├── requirements.txt
├── data/
├── faiss_index/
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Akshay132690/govassist-ai.git
cd govassist-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Build Vector Database

```bash
python ingest.py
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:
- Home Page
- Eligibility Checker
- AI Response Interface

---

## 🔮 Future Enhancements

- Multilingual support
- Source citations
- Chat history
- Scheme comparison
- Voice interaction
- Real-time government portal integration

---

## 📌 Key Learnings

- Retrieval-Augmented Generation (RAG)
- Vector Databases (FAISS)
- Embedding Models
- Semantic Search
- Prompt Engineering
- Streamlit Deployment
- Generative AI Application Development

---

## 👨‍💻 Author

Akshay Ingle

Computer Science Engineering Student

Interested in:
- Artificial Intelligence
- Machine Learning
- Generative AI
- Full Stack Development
