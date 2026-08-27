from flask import Flask, jsonify
from repository.personaje_repository import obtener_todos

app = Flask(__name__)

@app.route('/personajes', methods=['GET'])
def get_personajes():
    lista = obtener_todos()
    return jsonify(lista)

if __name__ == '__main__':
    app.run(debug=True, port=5000)