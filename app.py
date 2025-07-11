import streamlit as st
from summarizer import generate_summary
from utils import extract_text_from_docx
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Meeting Minutes Summarizer", layout="centered")

st.title("📝 Meeting Minutes Summarizer")

uploaded_file = st.file_uploader("Upload a .docx meeting transcript", type="docx")

summary_type = st.selectbox(
    "Choose summary type:",
    ["Executive Summary", "Detailed Notes", "Bullet Points Only"]
)

if uploaded_file:
    transcript = extract_text_from_docx(uploaded_file)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(transcript, summary_type)
            st.subheader("📋 Generated Summary")
            st.text_area("Output", value=summary, height=400)
            st.success("Done! Copy and paste or save as needed.")
