import pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()

def chunker(document):
    text_spliitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,  # bytes
        chunk_overlap =  30,
        len_function = len,
        is_separator_regex=False,
    )
    return text_spliitter.split_documents(document)
     

def sentence_extractor(chunks):
    """Extract sentences from a list of chunks"""

    sentences = []
    for chunk in chunks:
        sentences.append(chunk.page_content)
    
    return sentences
