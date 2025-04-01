import os
import logging
import zipfile
from utils.config import DOWNLOAD_DIR, ZIP_FILE

def zip_files():
    # Compacta os PDFs em um único arquivo ZIP.
    if not os.listdir(DOWNLOAD_DIR):
        logging.warning("Nenhum arquivo para compactar.")
        return
    logging.info("Compactando arquivos em ZIP")
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in os.listdir(DOWNLOAD_DIR):
            zipf.write(os.path.join(DOWNLOAD_DIR, file), arcname=file)
    logging.info(f"Arquivos compactados em {ZIP_FILE}")
