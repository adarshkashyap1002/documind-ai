# 🧠 DocuMind AI — Intelligent PDF Q&A System

> Upload any PDF. Ask questions in plain English. Get answers powered by Google Gemini AI.

## 🔗 Live Demo
**[Try it here → adarshpdfreaderai.streamlit.app](https://adarshpdfreaderai.streamlit.app)**

## 📌 What It Does
- Upload any PDF document — resume, textbook, contract, report
- Ask questions about the document in plain English
- Gemini AI reads the document and answers accurately
- Answers grounded strictly in your document — no hallucination
- Full chat-style interface with conversation history

## 🧠 How It Works
1. User uploads a PDF → PyPDF2 extracts all text
2. Text is passed as context to Gemini API with the user's question
3. Gemini answers strictly from the document context (RAG pattern)
4. Answer displayed in chat UI with session history maintained

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.0 Flash |
| PDF Processing | PyPDF2 |
| Language | Python 3.11 |
| Deployment | Streamlit Cloud |

## 🚀 Run Locally
```bash
git clone https://github.com/adarshkashyap1002/documind-ai
cd documind-ai
pip install streamlit google-genai PyPDF2
streamlit run app.py
```

## 👤 Author
**Adarsh Kashyap** — [LinkedIn](https://linkedin.com/in/adarshkashyap1002) | [GitHub](https://github.com/adarshkashyap1002)
