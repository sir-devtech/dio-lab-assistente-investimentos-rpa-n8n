# Assistente de investimentos com RPA, n8n e IA

Fork do lab da DIO. Eu completei o fluxo: o Python lê os clientes, o n8n cruza com o CSV e devolve uma mensagem por perfil. O print da execução está em `docs/execucao.png`.

## O que já funciona (MVP)

1. RPA em `rpa/extrair_clientes.py` (e o notebook com o webhook ligado).
2. Workflow em `n8n/workflow.json`: Webhook → HTTP (CSV) → Code → Respond.
3. Cruzamento real Conservador / Moderado / Arrojado com o produto do CSV.
4. Print da execução com os 4 nós em sucesso e 10 itens na resposta.

Página: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/

CSV: https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/data.csv

## Como rodar

1. `n8n start`
2. Importar `n8n/workflow.json` e publicar o fluxo.
3. `pip install requests beautifulsoup4`
4. `python rpa/extrair_clientes.py`

Webhook padrão: `http://127.0.0.1:5678/webhook/clientes`

## Prints

![Execução](docs/execucao.png)

Mais prints em `docs/prints/`.

## Desafio com Gemini e Gmail

A aula segue com LLM gerando o texto do e-mail e o nó Gmail enviando. Eu tenho a chave Gemini e o próximo passo é:

1. Criar a credencial Gemini no n8n (não colar a chave no README).
2. Trocar/estender o nó de mensagem para o modelo gerar o texto.
3. Conectar o Gmail na conta e validar o envio.

## Decisão técnica

A mensagem do MVP sai do Code com os dados do cliente e do CSV, sem pagar API. Assim o print fecha. A IA entra no desafio completo, em cima desse mesmo fluxo.
