from src.extractor import get_pdf_links
from src.downloader import download_pdfs
from src.compressor import zip_files
from utils.logger import setup_logging

# Configuração de logging
setup_logging()

# URL de origem
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

if __name__ == "__main__":
    pdf_links = get_pdf_links(URL)
    download_pdfs(pdf_links)
    zip_files()
