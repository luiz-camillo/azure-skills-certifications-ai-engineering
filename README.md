# Azure Skills — AI Engineering

Estudos e laboratórios práticos de engenharia de IA no **Microsoft Azure**, em Python.

## Conteúdo

- **Azure Language**: detecção de idioma, NER (entidades) e PII (dados pessoais)
- **Agentes no Microsoft Foundry**: agente de análise de texto com servidor MCP
- **Modelos de fala**: geração de voz (text-to-speech) e transcrição (speech-to-text)
- **Modelos de chat**: chamadas à Responses API com o SDK da OpenAI

## Tecnologias

Python · Microsoft Foundry · Azure Language · Azure OpenAI · SDKs `openai`, `azure-ai-projects`, `azure-ai-textanalytics`, `azure-identity`

## Como rodar

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure as variáveis de ambiente (endpoint, chave, nome do deployment) ou faça `az login`
4. Rode o script: `python nome_do_script.py`

> ⚠️ Nunca suba chaves ou arquivos `.env` para o repositório.
