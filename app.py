from flask import Flask, request, render_template, abort

app = Flask(__name__)

last_players = "Aguardando conexão..."

# Agora aceita GET também, para podermos capturar o acesso via navegador
@app.route("/webrequest", methods=["POST", "GET"])
def webrequest():
    # Se for navegador (GET), finge que a página não existe (404)
    if request.method == "GET":
        abort(404)

    # Se for POST (o jogo enviando dados), processa normalmente
    global last_players
    content = request.form.get("content")
    
    if content:
        last_players = content
        print(f"Update recebido: {last_players}")
    
    return ""

@app.route("/")
@app.route("/players")
def index():
    return render_template("index.html", players=last_players)

# Esse manipulador captura o abort(404) ou qualquer URL errada
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
