from pypdf import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st

def load_pdf(path):
    #loader = PyPDFLoader(path)
    #return loader.load()

    reader = PdfReader(path)
    return reader

def chunker(document):
    text_spliitter = RecursiveCharacterTextSplitter(
        chunk_size=512,  # bytes
        chunk_overlap =  30,
        #len_function = len,
        #is_separator_regex=False,
    )
    return text_spliitter.split_documents(document)
     

def sentence_extractor(chunks):
    """Extract sentences from a list of chunks"""

    sentences = []
    for chunk in chunks:
        sentences.append(chunk.page_content)
    
    return sentences

def text_extractor(reader):
    page_text = []
    for page in reader.pages:
        page_text.append(page.extract_text())
    
    return page_text

@st.cache_data
def pdf_parser(path):
    pdf = load_pdf(path)
    # chunks = chunker(pdf)
    
    # return sentence_extractor(chunks)

    return text_extractor(pdf)