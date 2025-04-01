import pdfplumber
import logging
from typing import List

def extrair_tabela(pdf_path: str, start_page: int = 3) -> List[List[str]]:
    # Extrai tabelas de um PDF a partir da página especificada.
    dados_extraidos = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i in range(start_page - 1, len(pdf.pages)):
                tabela = pdf.pages[i].extract_table()
                if tabela:
                    for linha in tabela:
                        if linha:
                            dados_extraidos.append([celula.strip().replace('\n', ' ') if celula else "" for celula in linha])
    except Exception as e:
        logging.error(f"Erro ao extrair tabela: {e}")
        raise
    
    if not dados_extraidos:
        logging.warning("Nenhuma tabela extraída. Verifique o arquivo PDF.")
        raise ValueError("Erro: Nenhuma tabela extraída do PDF.")
    
    return dados_extraidos
