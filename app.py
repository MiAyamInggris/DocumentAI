import streamlit as st
from utils import extract_text_from_pdf
from model import generate_summary

st.title("Testing The app")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Proses Ekstraksi Teks
    text = extract_text_from_pdf("temp.pdf")
    st.subheader("Testing Preview")
    st.write(text[:500] + "...")  # Show first 500 characters

    if st.button("Summarize"):
        summary = generate_summary(text)
        st.subheader("Summary")
        st.write(summary)