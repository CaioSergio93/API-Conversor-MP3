import os
import PyPDF2
import pyttsx3

import conversor
import leitor_texto

from flask import Flask, abort, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

@app.route("/teste", methods=["POST"])
class ConversaoResource(Resource):

    def post(self):
        dados = request.get_json()
        caminho_do_arquivo = dados.get("caminho_do_arquivo")

        if not caminho_do_arquivo:
            return jsonify({"erro": "Caminho do arquivo ausente nos dados da solicitação"}), 400

        try:
            conversor = ConversaoResource(caminho_do_arquivo)
            conversor.convert_to_mp3()
            caminho_de_saída = conversor.caminho_de_saída
            return jsonify({"caminho_de_saída": caminho_de_saída}), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
        
@app.route("/")
def hello_world():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(port=1515)    