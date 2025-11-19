from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def get_users():
    users = [
        {"id": 1, "nome": "Lucas sukar"},
        {"id": 2, "nome": "rodrigo torres"},
        {"id": 3, "nome": "caio lima"}
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
