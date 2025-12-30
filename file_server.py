from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    file.save(file.filename)
    return "Arquivo recebido com sucesso!\n"

app.run(host="0.0.0.0", port=5000)

