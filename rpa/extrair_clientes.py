"""
RPA: le a lista de clientes na pagina da DIO e envia para o webhook do n8n.
"""

import json
import sys

import requests
from bs4 import BeautifulSoup

URL_PAGINA = "https://digitalinnovationone.github.io/dio-lab-assistente-investimentos-rpa-n8n/"
N8N_WEBHOOK = "http://127.0.0.1:5678/webhook/clientes"


def extrair_clientes(url: str = URL_PAGINA) -> list[dict]:
    html = requests.get(url, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")
    linhas = soup.select("#clientes tbody tr")

    clientes = []
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) < 4:
            continue
        clientes.append(
            {
                "nome": colunas[0].get_text(strip=True),
                "email": colunas[1].get_text(strip=True),
                "saldo": colunas[2].get_text(strip=True),
                "perfil": colunas[3].get_text(strip=True),
            }
        )
    return clientes


def enviar_para_n8n(clientes: list[dict], webhook: str = N8N_WEBHOOK) -> requests.Response:
    resposta = requests.post(webhook, json={"clientes": clientes}, timeout=60)
    resposta.raise_for_status()
    return resposta


def main() -> int:
    clientes = extrair_clientes()
    print(f"Clientes encontrados: {len(clientes)}")
    for cliente in clientes:
        print(cliente)

    print(f"\nEnviando para {N8N_WEBHOOK} ...")
    resposta = enviar_para_n8n(clientes)
    print(f"Status HTTP: {resposta.status_code}")

    try:
        dados = resposta.json()
        print(json.dumps(dados, ensure_ascii=False, indent=2))
    except ValueError:
        print(resposta.text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
