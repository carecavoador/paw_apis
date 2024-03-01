"""
inplac.py
"""

from pathlib import Path

from validadores.utils import generate_texts_from_image_pdf

ID_CAMADA = "Impressão"
ID_ESPESSURA = "Espessura do Clichê: "
ID_FECHAMENTO = "Fechamento de Cilindro: "
ID_COD_BARRAS = "Código de Barras: "


def scan_lines(text: str) -> dict:
    result = {}

    lines = text.splitlines()
    for line in lines:
        # CAMADA --------------------------------------------------------------
        if line.startswith(ID_CAMADA):
            if "interna" in line.lower():
                result["camada"] = "interna"
            elif "externa" in line.lower():
                result["camada"] = "externa"

        # ESPESSURA -----------------------------------------------------------
        if line.startswith(ID_ESPESSURA):
            if "1,14" in line:
                result["espessura"] = 1.14
            elif "2,84" in line:
                result["espessura"] = 2.84

        # FECHAMENTO ----------------------------------------------------------
        if line.startswith(ID_FECHAMENTO):
            fechamento = line[len(ID_FECHAMENTO) :]
            try:
                fechamento = fechamento.replace(",", ".")
                fechamento = float(fechamento)
            except ValueError:
                fechamento = None
            if fechamento:
                result["fechamento"] = fechamento

        # CÓDIGO DE BARRAS ----------------------------------------------------
        if line.startswith(ID_COD_BARRAS):
            cod_barras = line[len(ID_COD_BARRAS) :]
            if cod_barras:
                result["cod_barras"] = cod_barras

    return result


def get_info(pdf: Path) -> dict:
    text = generate_texts_from_image_pdf(pdf)
    return scan_lines(text)
