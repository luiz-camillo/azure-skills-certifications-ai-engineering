


# pip install "azure-ai-projects>=2.1.0


from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://ai-apps-and-agents-azur-resource.services.ai.azure.com/api/projects/ai-apps-and-agents-azure"
agent_name = "computing-historian"
user_message = "Olá, me fale sobre o computador mais importante da história da computação, procure primeiramente na sua base de informações, se não tiver informação busque na web através da ferramenta disponível, e me fale junto com a resposta qual foi a sua fonte."


with (
  DefaultAzureCredential() as credential,
  AIProjectClient(
    endpoint=endpoint,
    credential=credential,
    allow_preview=True,
  ) as project_client,
):

  openai_client = project_client.get_openai_client(agent_name=agent_name)

  conversation = openai_client.conversations.create()
  response = openai_client.responses.create(
    conversation=conversation.id,
    input=[{"role": "user", "content": user_message}],
  )

  print(f"Retorno do modelo: {response.output_text}")