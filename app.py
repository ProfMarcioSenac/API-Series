from flask import Flask
from controllers.serie_controller import SerieController

app = Flask(__name__)

@app.route('/series', methods=['GET'])
def listar_todas():
    return SerieController.mostrar_tudo()

if __name__ == '__main__':
    app.run(debug=True)
