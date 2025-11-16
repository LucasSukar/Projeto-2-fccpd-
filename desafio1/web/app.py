from flask import Flask, jsonify, request
import socket
import datetime
app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    now = datetime.datetime.utcnow().isoformat() 
    return jsonify({
        "messagem": "oi (do container flask)!",
        "hostname": hostname,
        "tempo": now,
        "client_host": request.remote_addr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
