import streamlit as st

from utils.pdf import *
from utils.embedding import *
from utils.qa import *
import os


# sentences = None

# # Using "with" notation
# with st.sidebar:
#     uploaded_file = st.file_uploader("Choose a file")
#     if uploaded_file is not None:
#         temp_file = "./temp.pdf"
#         with open(temp_file, "wb") as file:
#             file.write(uploaded_file.getvalue())
#             file_name = uploaded_file.name
    
#         sentences = pdf_parser(temp_file)
sentences = []
if 'docs' in st.session_state:
    sentences = st.session_state['docs']

page = None
with st.container():
    option = st.selectbox(
    'Select A page to generate Q&A Pairs',
    [ i for i in range(len(sentences))] )

if option is not None:
    st.write(sentences[option])
    page = sentences[option]


prompt = st.chat_input('Ask me  something')

if prompt:
    with st.chat_message('Bot'):
        #st.write(ask_llm(prompt,top_k_sentences))
        st.write(grok_llm_qa(page,prompt))