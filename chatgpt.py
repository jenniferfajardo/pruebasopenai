import os
import PyPDF2
import re
import openai

pdf_sumary_text= ""

pdf_file_path= "./resources/paper.pdf"
pdf_file=open(pdf_file_path,"rb")
pdf_reader=PyPDF2.PdfReader(pdf_file)

openai.api_key=""

while True:

    prompt=input("Introduce una pregunta: \n")
    
    if prompt=="exit":
        break

    response=openai.Completion.create(engine="text-davinci-003",
                                       prompt=prompt ,
                                       max_tokens=1000)

    print(response.choices[0].text)