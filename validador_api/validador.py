import datetime as dt
from pathlib import Path

from flask import Flask, render_template, request
from validadores import inplac

app = Flask(__name__)

UPLOADS_FOLDER = Path(__file__).parent.joinpath("uploads")


@app.route("/novo")
def validador_inplac() -> str:
    return render_template("upload_os.html")


@app.route("/extrair", methods=["POST"])
def extrair_infos() -> str:
    cliente = request.form["cliente"]
    if not cliente:
        return "Nenhum cliente informado."

    try:
        file = request.files["ordem"]
        agora = dt.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        caminho = (
            Path(UPLOADS_FOLDER).joinpath(cliente).joinpath(agora).with_suffix(".pdf")
        )
        caminho.parent.mkdir(exist_ok=True)
        file.save(caminho)
        result = inplac.get_info(caminho)
    except KeyError:
        return "Nenhum arquivo selecionado."

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
