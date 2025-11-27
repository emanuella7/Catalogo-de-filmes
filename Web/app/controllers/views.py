from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Rota / funcionando"


@app.route('/filmes')
def listar_filmes():
    filmes = [
        {"id": 1, "titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"},
        {"id": 2, "titulo": "Inception", "ano": 2010, "diretor": "Christopher Nolan"}
    ]
    return render_template("filmes.html", filmes=filmes)

@app.route('/editar/<int:id>', methods=['GET'])
def editar_form(id):
    filme = {"id": id, "titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"}
    return render_template("editar.html", filme=filme)

@app.route('/editar/<int:id>', methods=['POST'])
def editar_filme(id):
    titulo = request.form['titulo']
    ano = request.form['ano']
    diretor = request.form['diretor']

    print("EDITANDO:", id, titulo, ano, diretor)

    return redirect('/filmes')

from flask import Blueprint, render_template, request, redirect

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/filmes')
def listar_filmes():
    filmes = [
        {"id": 1, "titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"},
        {"id": 2, "titulo": "Inception", "ano": 2010, "diretor": "Christopher Nolan"}
    ]
    return render_template("filmes.html", filmes=filmes)

@views.route('/editar/<int:id>', methods=['GET'])
def editar_form(id):
    filme = {"id": id, "titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"}
    return render_template("editar.html", filme=filme)

@views.route('/editar/<int:id>', methods=['POST'])
def editar_filme(id):
    titulo = request.form['titulo']
    ano = request.form['ano']
    diretor = request.form['diretor']

    print("EDITANDO:", id, titulo, ano, diretor)

    return redirect('/filmes')
