from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)
