from flask import Flask
app = Flask(__name__)
import google.generativeai as genai
api_key = 'AIzaSyDKeQ_CJEQdsiWSAja0C_X7veyARfITgxY'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
print("Created model!!")
@app.route('/')
def hello_world():
    response = model.generate_content("Who will win Andhra Pradesh elections")
    return response.text
