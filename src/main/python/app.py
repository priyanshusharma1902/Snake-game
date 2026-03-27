import os
from flask import Flask, render_template, request, jsonify
from game_logic import init_game, move_snake

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, '../../../templates'),
    static_folder=os.path.join(BASE_DIR, '../../../static')
)

game_state = init_game()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["GET"])
def start():
    global game_state
    game_state = init_game()
    return jsonify(game_state)

@app.route("/move", methods=["POST"])
def move():
    global game_state
    data = request.json
    game_state["direction"] = data["direction"]
    game_state = move_snake(game_state)
    return jsonify(game_state)

if __name__ == "__main__":
    app.run(debug=True)
