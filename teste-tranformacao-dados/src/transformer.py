import pandas as pd
from typing import List

def criar_dataframe(tabela_dados: List[List[str]]) -> pd.DataFrame:
    # Cria um DataFrame a partir dos dados extraídos.
    colunas = [
        "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB", "HCO",
        "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
    ]
    df = pd.DataFrame(tabela_dados, columns=colunas)
    df = df[df["PROCEDIMENTO"] != "PROCEDIMENTO"] 
    return df

def substituir_abreviacoes(df: pd.DataFrame) -> pd.DataFrame:
    # Substitui abreviações nas colunas OD e AMB.
    return df.replace({"OD": {"OD": "Seg. Odontológica"}, "AMB": {"AMB": "Seg. Ambulatorial"}})
