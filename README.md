# Simple RAG PDF Q&A Demo

This project demonstrates a minimal Retrieval-Augmented Generation (RAG) pipeline using Streamlit and OpenAI for Q&A over a PDF document.

## Features
- Upload a PDF
- Ask questions about its content
- Uses OpenAI GPT for answers

## Setup
1. Clone this repo and add your PDF (e.g., `budget_speech_2025.pdf`).
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_key
   ```
3. Install dependencies:
   ```
   pip install streamlit openai PyPDF2 python-dotenv
   ```

## Usage
Run the Streamlit app:
```sh
streamlit run app.py
```
Upload your PDF and ask questions interactively.

## Files
- `app.py`: Main Streamlit app
- `pdf_loader.py`: PDF text extraction utility
- `budget_speech_2025.pdf`: Example PDF

## Notes
- This is a minimal demo for educational purposes.
- For production, use more advanced chunking and retrieval methods.
