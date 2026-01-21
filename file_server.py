import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    storage_path = os.path.join('storage', file.filename)

    if not os.path.exists('storage'):
        os.makedirs('storage')

    file.save(storage_path)
    return "Arquivo recebido com sucesso em: " + storage_path + "\n"

app.run(host="0.0.0.0", port=5000)
