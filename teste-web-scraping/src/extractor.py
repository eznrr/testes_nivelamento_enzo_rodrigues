import logging
import requests
from bs4 import BeautifulSoup

def get_pdf_links(url):
    # Obtém os links dos PDFs da página alvo.
    logging.info("Acessando a página para extrair os links dos PDFs.")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a página: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [
        link["href"].strip() if link["href"].startswith("http") else "https://www.gov.br" + link["href"].strip()
        for link in soup.find_all("a", href=True)
        if link["href"].endswith(".pdf") and ("Anexo I" in link.get_text(strip=True) or "Anexo II" in link.get_text(strip=True))
    ]

    logging.info(f"Foram encontrados {len(pdf_links)} PDFs para download.")
    return pdf_links
