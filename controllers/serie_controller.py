from flask import jsonify
from models.serie import SerieModel

class SerieController:
    @staticmethod
    def mostrar_tudo():
        series = SerieModel.get_all()
        return jsonify(series)