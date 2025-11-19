from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_A_URL = "http://service_a:5000/users"   


@app.route("/info")
def combined_info():
    try:
        response = requests.get(SERVICE_A_URL)
        users = response.json()

        result = []
        for user in users:
            result.append({
                "mensagem": f"Usuário {user['nome']} ativos na faculdade desde 2023.2."
            })

        return jsonify(result)

    except Exception as e:
        return jsonify({"erro": "Não foi possível acessar o Service A", "detalhe": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
