import pandas as pd
import zipfile
import os
import logging

def salvar_csv(df: pd.DataFrame, filename: str) -> None:
    # Salva o DataFrame em um arquivo CSV.
    df.to_csv(filename, index=False, encoding='utf-8', sep=';')
    logging.info(f"Arquivo CSV gerado: {filename}")

def compactar_arquivo(csv_filename: str, zip_filename: str) -> None:
    # Compacta o arquivo CSV em um ZIP e gerencia a remoção do CSV.
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_filename)
        logging.info(f"Arquivo ZIP gerado: {zip_filename}")
    except Exception as e:
        logging.error(f"Erro ao compactar arquivo: {e}")
        raise
    finally:
        if os.path.exists(csv_filename):
            os.remove(csv_filename)
            logging.info(f"Arquivo CSV removido: {csv_filename}")
