from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    data = [
        {"id": 101, "user_id": 1, "possui": "carro"},
        {"id": 102, "user_id": 2, "possui": "moto"},
        {"id": 103, "user_id": 1, "possui": "bicicleta"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
