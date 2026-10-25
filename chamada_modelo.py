
#necessário instalar o SDK openai
#pip install openai

#importando bibliotecas

import os
from openai import OpenAI

#montando cliente para ser usado na chamada da api após varíaveis declaradas no terminal

# a variavel cliente vai conter a url do endpoint da azure e a chave de api da azure
#toda vez que precisar fazer a chamada de api ele usa essas credenciais no padrao da openai

client = OpenAI(
    base_url=os.environ['AZURE_OPENAI_ENDPOINT'],
    api_key=os.environ['AZURE_API_KEY']
)

#em response temos a chamada da api

response = client.responses.create(
    model=os.environ['DEPLOYMENT_NAME'],
    input=[{"role" : "system", "content": "Você é um agente que só responde perguntas sobre o 11 de setembro apenas. Se perguntarem algo diferente vc responde que não pode revelar porque a pergunta viola as diretrizes"},
           {"role" : "user", "content": "Quero saber quem foi o reponsável pelo 11 de setembro"}],
    max_output_tokens=500
)


print(response.output_text)

print('\n')

print(response.model)

print('\n')

print(response.usage)
