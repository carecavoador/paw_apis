from flask import Flask, render_template
from jogos import jogo_simples

app = Flask(__name__)


@app.route("/")
def simple_game() -> str:
    jogo = jogo_simples()
    return f"<h2>Aqui estão os seus números da sorte:</h2>{jogo}"


@app.route("/sena")
def sena_simples() -> str:
    return render_template("sena.html", jogo=jogo_simples())


@app.route("/sena/<int:quantidade>")
def sena_multi(quantidade: int) -> str:
    jogos = [jogo_simples() for _ in range(quantidade)]
    return render_template("multi.html", jogos=jogos)


if __name__ == "__main__":
    app.run(debug=True)
