from flask import Flask, request
from controllers.serie_controller import SerieController

app = Flask(__name__)

@app.route('/series', methods=['GET'])
def listar_todas():
    return SerieController.mostrar_tudo()

@app.route('/series/<int:serie_id>', methods=['GET'])
def listar_por_id(serie_id):
    return SerieController.mostrar_por_id(serie_id)

@app.route('/series/titulo/<string:texto>', methods=['GET'])
def listar_por_titulo(texto):
    return SerieController.mostrar_por_titulo(texto)

@app.route('/series/categoria/<string:texto>', methods=['GET'])
def listar_por_categoria(texto):
    return SerieController.mostrar_por_categoria(texto)

@app.route('/series/idioma/<string:texto>', methods=['GET'])
def listar_por_idioma(texto):
    return SerieController.mostrar_por_idioma(texto)

@app.route('/series/pais/<string:texto>', methods=['GET'])
def listar_por_pais(texto):
    return SerieController.mostrar_por_pais(texto)

@app.route('/series', methods=['POST'])
def cadastrar_serie():
    dados = request.json
    return SerieController.cadastrar(dados)

@app.route('/series/<int:serie_id>', methods=['PUT'])
def atualizar_serie(serie_id):
    dados = request.json
    return SerieController.atualizar(serie_id, dados)

@app.route('/series/<int:serie_id>', methods=['DELETE'])
def excluir_serie(serie_id):
    return SerieController.excluir(serie_id)

if __name__ == '__main__':
    app.run(debug=True)
