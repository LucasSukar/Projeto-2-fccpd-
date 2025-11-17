from flask import Flask
import redis
import psycopg2
app = Flask(__name__)
@app.route("/")
def home():
    return "Serviço web ok"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host="db",
            user="admin",
            password="123",
            database="teste_desafio3"
        )
        conn.close()
        return "Banco ok"
    except Exception as e:
        return f"Erro banco: {str(e)}"

@app.route("/cache")
def cache_check():
    try:
        r = redis.Redis(host="cache", port=6379, decode_responses=True)
        r.set("teste", "ok")
        return "Redis ok"
    except Exception as e:
        return f"Erro redis: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
