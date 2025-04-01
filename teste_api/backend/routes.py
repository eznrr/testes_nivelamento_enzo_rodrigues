from flask import Blueprint, request, jsonify, Response
import json
import logging
import pandas as pd
from unidecode import unidecode 
import re
from dados import df

bp = Blueprint("api", __name__)

@bp.route("/buscar", methods=["GET"])
def buscar():
    nome = request.args.get("nome", "").strip()
    if not nome:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400

    logging.info(f"Buscando por: {nome}")

    try:
        nome_normalizado = unidecode(nome).lower()

        def calcular_relevancia(row):
            """Calcula a relevância da correspondência."""
            nome_operadora = unidecode(str(row["Nome_Completo"])).lower()
            
            if nome_operadora == nome_normalizado:
                return 3  
            elif nome_normalizado in nome_operadora:
                return 2 
            elif re.search(rf"\b{re.escape(nome_normalizado)}\b", nome_operadora):
                return 1  
            return 0 

        df["Relevancia"] = df.apply(calcular_relevancia, axis=1)

        resultados = df[df["Relevancia"] > 0].sort_values(by="Relevancia", ascending=False)

        if not resultados.empty:
            resultados_dict = resultados.drop(columns=["Relevancia"]).astype(str).to_dict(orient="records")

            json_data = json.dumps(resultados_dict[:10], ensure_ascii=False) 
            return Response(json_data, status=200, mimetype="application/json; charset=utf-8")
        else:
            return jsonify({"erro": "Nenhum resultado encontrado"}), 404

    except Exception as e:
        logging.error(f"Erro ao processar busca: {e}")
        return jsonify({"erro": "Erro interno no servidor"}), 500
