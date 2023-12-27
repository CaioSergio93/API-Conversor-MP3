import os
import PyPDF2
import pyttsx3

import conversor
import leitor_texto

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)

class Conversao(Resource):

    def post(self):
        data = request.get_json()
        file_path = data.get("file_path")

        converter = Conversao(file_path)
        converter.convert_to_mp3()

        return jsonify({"output_path": converter.output_path}), 200

api.add_resource(Conversao, "/convert")

app.run()
