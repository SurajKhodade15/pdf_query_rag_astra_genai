import streamlit as st
import openai
from pdf_loader import extract_pdf_text
import os
from dotenv import load_dotenv
from chromadb import Client
from chromadb.utils import embedding_functions

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("India Budget 2025 Q&A (RAG + Chroma DB)")

# Load PDF once
pdf_path = "budget_speech_2025.pdf"
raw_text = extract_pdf_text(pdf_path)
st.write("PDF loaded: India Budget 2025")

# Chunk PDF
chunk_size = 800
chunks = [raw_text[i:i+chunk_size] for i in range(0, len(raw_text), chunk_size)]

# Setup Chroma DB and OpenAI embedding
chroma_client = Client()
openai_embed_fn = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-ada-002"
)
collection = chroma_client.create_collection(name="budget2025", embedding_function=openai_embed_fn)

# Add chunks to Chroma DB (if not already added)
if collection.count() == 0:
    for idx, chunk in enumerate(chunks):
        collection.add(documents=[chunk], ids=[str(idx)])

sample_questions = [
    "What are the key highlights of the India Budget 2025?",
    "What is the fiscal deficit target for 2025?",
    "What are the major allocations for education?",
    "How much is allocated to healthcare?",
    "What are the new tax proposals?"
]

st.markdown("### Sample Questions:")
for q in sample_questions:
    st.button(q, key=q)

question = st.text_input("Or ask your own question:")

# If a sample question button is clicked, use that question
for q in sample_questions:
    if st.session_state.get(q):
        question = q

if question:
    # Retrieve top relevant chunks from Chroma
    results = collection.query(query_texts=[question], n_results=2)
    context = "\n".join(results["documents"][0])
    prompt = f"Answer the following question using the provided context.\nContext: {context}\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write("**Answer:**", response.choices[0].message.content)
