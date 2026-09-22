from flask import Flask, render_template, request, redirect, url_for
from repository.personaje_repository import obtener_todos, guardar
from models.personajes import Personaje
from services.personaje_service import validar_personaje

app = Flask(__name__)

@app.route('/personajes')
def listar_personajes():
    mis_personajes = obtener_todos()

    if not mis_personajes:
        mis_personajes = [{'nombre': 'Thadeo', 'clase': 'Guerrero', 'nivel': 5, 'vida': 20}]

    return render_template('personajes.html', personajes=mis_personajes)

@app.route('/personajes', methods=['POST'])
def crear_personaje():
    nombre = request.form.get('nombre')
    clase = request.form.get('clase')

    # Convertimos de forma segura DENTRO de la función para evitar el ValueError si vienen vacíos
    nivel_raw = request.form.get('nivel')
    nivel = int(nivel_raw) if nivel_raw and nivel_raw.isdigit() else 0

    vida_raw = request.form.get('vida')
    vida = int(vida_raw) if vida_raw and vida_raw.isdigit() else 0

    # 1. Llamamos al Servicio para validar
    errores = validar_personaje(nombre, clase, nivel, vida)

    # 2. Si hay errores, volvemos a mostrar la vista junto con la lista de personajes actual
    if errores:
        mis_personajes = obtener_todos()
        return render_template('personajes.html', errores=errores, personajes=mis_personajes)

    # 3. Solo si NO hubo errores, guardamos el personaje
    personaje = Personaje(nombre=nombre, clase=clase, nivel=nivel, vida=vida)
    guardar(personaje)

    return redirect('/personajes')

if __name__ == '__main__':
    app.run(debug=True, port=5000)