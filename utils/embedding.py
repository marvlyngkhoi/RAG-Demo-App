import requests
import numpy as np
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def query_similarity(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_score(sentences,words):
	
    score_results = query_similarity({
	    "inputs": {
		    "source_sentence": words,
		    "sentences":sentences

	        },
        })
    return score_results

def get_top_k(sentences,score,k):
    
    top_indices = np.argsort(score)[::-1][:k]
    top_K_sentences = ''
    for i in top_indices:
        sentences+=sentences[i]
    
    return top_K_sentences

@st.cache_data
def get_sentences(sentences,words,k=5):
    score = get_score(sentences,words)

    return  get_top_k(sentences,score,k)
     
