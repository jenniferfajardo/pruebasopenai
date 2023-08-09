import pdfplumber
from fastapi import FastAPI
from dotenv import load_dotenv
import openai
import os
from models.model import Prompt


app=FastAPI()
load_dotenv()

openai.api_key=os.getenv('SECRET_KEY')


@app.post("/chat")
def generate_response(prompt:Prompt):

    with open('conversacion.txt', 'r') as file:
        conversation = file.read()
    
    text_length=1000
    gpt3_model="text-davinci-003"
    response=openai.Completion.create(
        engine=gpt3_model,
        prompt=prompt.text,
        max_tokens=text_length,
        n=1,
        stop=None,
        temperature=0.5)
    
    return response.choices[0].text

pdf_path = 'terminacion.pdf'

@app.get("/leepdf")    
def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

pdf_text = extract_pdf_text(pdf_path)

while True:

    question=input("Haz tu pregunta: \n")
    custom_prompt = f"Documento PDF:\n{pdf_text}\n\nPregunta: {question}\nRespuesta:"

    if question=="exit":
        break

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=custom_prompt,
        max_tokens=100
        )

    print(response.choices[0].text.strip())


