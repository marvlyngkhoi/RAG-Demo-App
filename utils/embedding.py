import requests
import numpy as np


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

def get_top_k(sentences,score,k):
    
    top_indices = np.argsort(score)[::-1][:k]
    top_K_sentences = ''
    for i in top_indices:
        sentences+=sentences[i]
    
    return top_K_sentences
    

