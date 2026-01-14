from flask import Flask, request, jsonify

app = Flask(__name__)

# guarda o último valor recebido
last_players = 0

@app.route("/webrequest", methods=["POST"])
def webrequest():
    global last_players

    content = request.form.get("content")

    if content and content.isdigit():
        last_players = int(content)
        print("Players atualizados:", last_players)
    else:
        print("POST inválido:", content)

    return ""

@app.route("/players", methods=["GET"])
def players():
    # JSON limpo e confiável
    return jsonify({
        "players": last_players
    })
    
@app.route("/players_api")
def players_api():
    return {
        "players": last_players
    }

@app.route("/")
def index():
    return "LAC WebRequest Online"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
