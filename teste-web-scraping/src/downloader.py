import os
import logging
import requests
from concurrent.futures import ThreadPoolExecutor
from utils.config import DOWNLOAD_DIR

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_pdf(link):
    # Faz o download de um único arquivo PDF, evitando downloads duplicados.
    filename = os.path.join(DOWNLOAD_DIR, os.path.basename(link))

    if os.path.exists(filename):
        logging.info(f"Arquivo já existe, pulando download: {filename}")
        return

    try:
        logging.info(f"Baixando {filename}")
        response = requests.get(link, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        if os.path.getsize(filename) == 0:
            logging.warning(f"Arquivo vazio detectado: {filename}")
            os.remove(filename)
            return False
        logging.info(f"Download concluído: {filename}")
    except requests.RequestException as e:
        logging.error(f"Erro ao baixar {filename}: {e}")

def download_pdfs(pdf_links):
    # Faz o download dos PDFs em paralelo para melhor desempenho.
    if not pdf_links:
        logging.warning("Nenhum link de PDF para baixar.")
        return
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_pdf, pdf_links)
