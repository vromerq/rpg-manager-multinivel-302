from flask import Flask, render_template
from repository.personaje_repository import obtener_todos
from flask import request, redirect
app = Flask(__name__)

@app.route('/personajes')
def listar_personajes():
    mis_personajes = obtener_todos() # O como se llame tu método

    if not mis_personajes:
        mis_personajes = [{'nombre': 'Thadeo', 'clase': 'Guerrero', 'nivel': 5}]

    return render_template('personajes.html', personajes=mis_personajes)


@app.route('/personajes', methods=['POST'])
def crear_personaje():
    nombre = request.form['nombre']
    clase = request.form['clase']
    nivel = int(request.form['nivel'])
    vida = int(request.form['vida'])

    from models.personajes import Personaje
    from repository.personaje_repository import guardar

    personaje = Personaje(nombre=nombre, clase=clase, nivel=nivel, vida=vida)
    guardar(personaje)

    return redirect('/personajes')

if __name__ == '__main__':
    app.run(debug=True, port=5000)