from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    data = [
        {"id": 1, "nome": "andre castro"},
        {"id": 2, "nome": "Caio lima"},
        {"id": 3, "nome": "lucas sukar"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
