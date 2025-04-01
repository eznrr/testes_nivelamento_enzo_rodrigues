import os
import logging

def verificar_arquivo(path: str) -> None:
    # Verifica se o arquivo existe no caminho especificado.
    if not os.path.exists(path):
        logging.error(f"Arquivo não encontrado: {path}")
        raise FileNotFoundError(f"O arquivo {path} não foi encontrado.")
