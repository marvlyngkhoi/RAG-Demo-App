import requests
from groq import Groq

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": "Bearer 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"}




client = Groq(
    api_key="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",
)

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

def grok_llm(context,question):
    
    chat_completion = client.chat.completions.create(
    messages=[
         {
            "role": "system",
            "content": f"you are a helpful assistant. that answer the question based on the context {context}"
        },
        {
            "role": "user",
            "content":question,
        }
    ],
    model="mixtral-8x7b-32768", 
    )

    return chat_completion.choices[0].message.content

def grok_llm_qa(context,question):
    
    chat_completion = client.chat.completions.create(
    messages=[
         {
            "role": "system",
            "content": f"you are a helpful assistant that generate  questions and answer pairs based on the context {context}"
        },
        {
            "role": "user",
            "content":question,
        }
    ],
    model="mixtral-8x7b-32768", 
    )

    return chat_completion.choices[0].message.content


      
    