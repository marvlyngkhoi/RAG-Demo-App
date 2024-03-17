import streamlit as st

from utils.pdf import *
from utils.embedding import *
from utils.qa import *
import os


sentences = None

# Using "with" notation
with st.sidebar:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        temp_file = "./temp.pdf"
        with open(temp_file, "wb") as file:
            file.write(uploaded_file.getvalue())
            file_name = uploaded_file.name
    
        sentences = pdf_parser(temp_file)

    
keywords = None
top_k_sentences=None
with st.container():
    keywords = st.text_input('Keywords')
    if keywords is not None and sentences is not None:
        st.write(keywords)
        top_k_sentences = get_sentences(sentences,keywords,k=5)
        st.write(top_k_sentences)

prompt = st.chat_input('Say something')

if prompt:
    with st.chat_message('Bot'):
        st.write(ask_llm(prompt,top_k_sentences))