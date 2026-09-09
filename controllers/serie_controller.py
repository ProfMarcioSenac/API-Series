from flask import jsonify
from models.serie import SerieModel

class SerieController:
    @staticmethod
    def mostrar_tudo():
        series = SerieModel.get_all()
        return jsonify(series)

    @staticmethod
    def mostrar_por_id(serie_id):
        serie = SerieModel.get_by_id(serie_id)
        if serie:
            return jsonify(serie)
        return jsonify({"erro": "Série não encontrada"}), 404

    @staticmethod
    def mostrar_por_titulo(texto):
        series = SerieModel.get_by_title(texto)
        if series:
            return jsonify(series)
        return jsonify({"erro": "Série não encontrada"}), 404

    @staticmethod
    def mostrar_por_categoria(texto):
        series = SerieModel.get_by_category(texto)
        if series:
            return jsonify(series)
        return jsonify({"erro": "Categoria não encontrada"}), 404