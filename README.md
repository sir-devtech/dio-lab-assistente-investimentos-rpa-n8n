# Assistente de investimentos com RPA, n8n e IA

Fork do lab da DIO. O Python lê os clientes, o n8n cruza com o CSV, a Gemini gera o e-mail e o Gmail envia. Print da execução em `docs/execucao.png`.

## O que já funciona

1. RPA em `rpa/extrair_clientes.py` (e o notebook com o webhook ligado).
2. Workflow em `n8n/workflow.json`:
   Webhook → HTTP (CSV) → Cruzar perfil → Gemini Email → Montar e-mail → IF → Enviar Gmail → Preparar resposta → Respond.
3. Cruzamento Conservador / Moderado / Arrojado (case-insensitive) com o produto do CSV.
4. Texto gerado por `gemini-3.5-flash-lite` via HTTP + credencial Gemini.
5. Envio real pelo nó **Gmail** com OAuth2.
6. Prints em `docs/prints/` (incluindo execução com Gemini + Gmail).

Página: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/

CSV: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/data.csv

## Como rodar

1. `n8n start`
2. Importar `n8n/workflow.json`.
3. Criar credenciais no n8n (não colar chaves no repositório):
   - **Google Gemini (PaLM) Api**
   - **Gmail OAuth2 API** (ative a Gmail API no Google Cloud e adicione seu e-mail como usuário de teste)
4. Publicar o fluxo.
5. `pip install requests beautifulsoup4`
6. `python rpa/extrair_clientes.py`

Webhook padrão: `http://127.0.0.1:5678/webhook/clientes`

## Prints

![Execução](docs/execucao.png)

Mais prints em `docs/prints/`.

## Decisão técnica

- LangChain/`lmChatGoogleGemini` ficou instável nesta versão do n8n.
- A chamada HTTP `generateContent` com `gemini-3.5-flash-lite` gerou o texto com estabilidade.
- O nó Gmail envia `email_to` / `assunto` / `corpo_email` e a resposta do webhook marca `email_enviado`.
