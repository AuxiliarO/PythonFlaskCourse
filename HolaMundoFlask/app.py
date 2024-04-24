from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'


# http://localhost:5000/
@app.route("/")
def inicio():

    if 'username' in session:
        return 'El usuario ya ha realizado un login'
    return 'Login no realizado'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #ToDo validación usuario contraseña
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('inicio'))

    return render_template('login.html')


@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Billy'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def error_404(error):
    return render_template('error404.html', error=error), 404


# REST Response
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mosstrar_json(nombre):
    valores = {
        "nombre": nombre,
        "edad": 25,
        "pais": "Colombia"
    }
    return jsonify(valores)
