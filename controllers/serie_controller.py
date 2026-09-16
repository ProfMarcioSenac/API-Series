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

    @staticmethod
    def mostrar_por_idioma(texto):
        series = SerieModel.get_by_language(texto)
        if series:
            return jsonify(series)
        return jsonify({"erro": "Idioma não encontrado"}), 404

    @staticmethod
    def mostrar_por_pais(texto):
        series = SerieModel.get_by_country(texto)
        if series:
            return jsonify(series)
        return jsonify({"erro": "País não encontrado"}), 404

    @staticmethod
    def cadastrar(dados):
        novo_id = SerieModel.insert(dados)
        return jsonify({"mensagem": "Série criada com sucesso", "id": novo_id}), 201

    @staticmethod
    def atualizar(serie_id, dados):
        sucesso = SerieModel.update(serie_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Série atualizada com sucesso"})
        return jsonify({"erro": "Série não encontrada", "código": "404"}), 404

    @staticmethod
    def excluir(serie_id):
        sucesso = SerieModel.delete(serie_id)
        if sucesso:
            return jsonify({"mensagem": "Série excluída com sucesso"})
        return jsonify({"erro": "Série não encontrada", "código": "404"}), 404