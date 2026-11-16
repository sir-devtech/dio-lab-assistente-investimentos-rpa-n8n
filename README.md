# Assistente de investimentos com RPA, n8n e IA

Fork do lab da DIO. O Python lê os clientes, o n8n cruza com o CSV, a Gemini gera o corpo do e-mail e a resposta volta no webhook. Print da execução em `docs/execucao.png`.

## O que já funciona

1. RPA em `rpa/extrair_clientes.py` (e o notebook com o webhook ligado).
2. Workflow em `n8n/workflow.json`:
   Webhook → HTTP (CSV) → Cruzar perfil → Gemini Email → Montar e-mail → IF → Respond.
3. Cruzamento Conservador / Moderado / Arrojado (case-insensitive) com o produto do CSV.
4. Texto do e-mail gerado por `gemini-3.5-flash-lite` via HTTP + credencial `googlePalmApi`.
5. Prints da execução com sucesso (incluindo Gemini) em `docs/prints/`.

Página: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/

CSV: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/data.csv

## Como rodar

1. `n8n start`
2. Importar `n8n/workflow.json`, criar a credencial **Google Gemini (PaLM) Api** e publicar o fluxo.
3. `pip install requests beautifulsoup4`
4. `python rpa/extrair_clientes.py`

Webhook padrão: `http://127.0.0.1:5678/webhook/clientes`

Não cole a API key no repositório nem no chat.

## Prints

![Execução](docs/execucao.png)

Mais prints em `docs/prints/`.

## Gmail (opcional / desafio completo)

O fluxo já devolve `email_to`, `assunto` e `corpo_email`. Para enviar de verdade:

1. Conectar credencial OAuth do Gmail no n8n.
2. Ligar o nó Gmail depois de **Montar e-mail** (ou no ramo `true` do IF).

## Decisão técnica

- LangChain/`lmChatGoogleGemini` ficou instável nesta versão do n8n (modelo antigo 404 / 3.8-flash travava).
- A chamada HTTP direta em `generateContent` com `gemini-3.5-flash-lite` fechou o desafio de IA com resposta rápida e estável.
