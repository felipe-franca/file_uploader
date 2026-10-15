import os
import socket
from flask import Flask, request

HOST = "0.0.0.0"
PORT = 5000

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    storage_path = os.path.join('storage', file.filename)

    if not os.path.exists('storage'):
        os.makedirs('storage')

    file.save(storage_path)
    return "Arquivo recebido com sucesso em: " + storage_path + "\n"

def local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"

def log_curl_example():
    print("Exemplo para enviar arquivo:")
    print(f'  curl -F "file=@arquivo.log" http://localhost:{PORT}/upload')
    print(f'  curl -F "file=@arquivo.log" http://{local_ip()}:{PORT}/upload')

log_curl_example()
app.run(host=HOST, port=PORT)
