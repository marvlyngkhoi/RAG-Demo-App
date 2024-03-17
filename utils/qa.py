import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def ask_llm(question,context):
    ans = query({
	    "inputs": f"""Use the following pieces of context to answer the question at the end.
                If you don't know the answer, just say that you don't know, don't try to make up an answer.
                {context}
                Question: {question}
                Helpful Answer:"""
        })

    return ans[0]['generated_text'].split(question)[1]
    