import logging
import os
from src.extractor import extrair_tabela
from src.transformer import criar_dataframe, substituir_abreviacoes
from src.saver import salvar_csv, compactar_arquivo
from utils.verifier import verificar_arquivo
from utils.logger import setup_logging
from utils.config import PDF_PATH, CSV_FILENAME, ZIP_FILENAME

# Configuração de logging
setup_logging()

def processar_pdf(pdf_path: str, csv_filename: str, zip_filename: str) -> None:
    # Executa o processo completo de extração e compactação.
    tabela_dados = extrair_tabela(pdf_path)
    df = criar_dataframe(tabela_dados)
    df = substituir_abreviacoes(df)
    salvar_csv(df, csv_filename)
    compactar_arquivo(csv_filename, zip_filename)

def main():
    # Função principal para iniciar o processo.
    verificar_arquivo(PDF_PATH)
    processar_pdf(PDF_PATH, CSV_FILENAME, ZIP_FILENAME)
    logging.info("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
