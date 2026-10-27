


#código para o curso da azure focado em IA nesse código irei chamar um agente através da api


from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

myEndpoint = "https://lazarettieb-7263-resource.services.ai.azure.com/api/projects/lazarettieb-7263"

project_client = AIProjectClient(
  endpoint=myEndpoint,
  credential=DefaultAzureCredential(),
)

myAgent = "agente47"

agent = project_client.agents.get(agent_name=myAgent)
print(f"O agente buscado é o {agent.name}")

openai_client = project_client.get_openai_client()

resposta = openai_client.responses.create(
  input=[{"role": "user", "content": "Me fale qual é a sua finalidade."}],
  extra_body={"agent_reference": {"name": agent.name, "type": "agent_reference"}},
)

print(f"Saída retornada: {resposta.output_text}")