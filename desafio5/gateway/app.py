from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URLs internas dos microsserviços (rede do docker-compose)
USERS_URL = "http://service_users:5000/users"
ORDERS_URL = "http://service_orders:5000/orders"


@app.route("/users")
def users():
    response = requests.get(USERS_URL)
    return jsonify(response.json())


@app.route("/orders")
def orders():
    response = requests.get(ORDERS_URL)
    return jsonify(response.json())

@app.route("/health")
def health():
    return {"status": "gateway ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
