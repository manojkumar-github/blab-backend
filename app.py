from flask import Flask, request
app = Flask(__name__)
#import google.generativeai as genai
#api_key = 'AIzaSyDKeQ_CJEQdsiWSAja0C_X7veyARfITgxY'
#genai.configure(api_key=api_key)
#model = genai.GenerativeModel('gemini-pro')
#print("Created model!!")


from langchain.llms import HuggingFaceHub
import os
from getpass import getpass

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'


llm = HuggingFaceHub(
    repo_id="huggingfaceh4/zephyr-7b-alpha", 
    model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
)


@app.route('/', methods=['POST'])
def bot_prompt():
    query = request.json.get('message')

    prompt = f"""
     <|system|>
    You are an AI assistant that follows instruction extremely well.
    Please be truthful and give direct answers
    </s>
     <|user|>
     {query}
     </s>
     <|assistant|>
    """
    response = llm.predict(prompt)
    return response
