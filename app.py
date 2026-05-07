import streamlit as st
from google import genai
import PyPDF2

st.set_page_config(page_title="DocuMind AI", page_icon="🧠", layout="wide")
st.title("🧠 DocuMind AI")
st.caption("Upload any PDF and ask questions in plain English")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def ask_gemini(api_key, context, question):
    client = genai.Client(api_key=api_key)
    prompt = f"""Answer the question based ONLY on the document below.
If answer not found, say "I couldn't find that in the document."

Document:
{context[:10000]}

Question: {question}
Answer:"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

if uploaded_file and api_key:
    with st.spinner("Reading document..."):
        text = extract_text(uploaded_file)
    st.success(f"✅ Document loaded — {len(text.split())} words extracted")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📄 Document Preview")
        st.text_area("", text[:2000] + "...", height=300)
    with col2:
        st.subheader("💬 Ask Anything")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        question = st.chat_input("Ask a question about your document...")
        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.write(question)
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = ask_gemini(api_key, text, question)
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
elif not api_key:
    st.info("👈 Enter your Gemini API key in the sidebar to get started")
elif not uploaded_file:
    st.info("👈 Upload a PDF in the sidebar")