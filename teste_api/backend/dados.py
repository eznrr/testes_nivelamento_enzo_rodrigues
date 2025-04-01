import pandas as pd
import logging

csv_path = "backend\csv\Relatorio_cadop.csv"

def carregar_dados():
    """Carrega e processa os dados do CSV, tratando possíveis erros."""
    try:
        df = pd.read_csv(csv_path, encoding="utf-8", sep=";")
        df = df.dropna(subset=["Razao_Social", "Nome_Fantasia"])
        df["Nome_Completo"] = df[["Razao_Social", "Nome_Fantasia"]].apply(lambda x: " ".join(x.dropna()), axis=1)
        logging.info("Dados carregados com sucesso!")
        return df
    except FileNotFoundError:
        logging.error(f"Arquivo {csv_path} não encontrado!")
        return pd.DataFrame()
    except Exception as e:
        logging.error(f"Erro ao carregar o CSV: {e}")
        return pd.DataFrame()

df = carregar_dados()
