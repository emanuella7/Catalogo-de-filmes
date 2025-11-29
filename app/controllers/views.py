import base64
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.Filme import Filme

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

# LISTAR FILMES
@views.route('/filmes')
def listar_filmes():
    filmes = Filme.query.order_by(Filme.id.desc()).all()
    return render_template("filmes.html", filmes=filmes)

# FORMULÁRIO ADICIONAR
@views.route('/adicionar', methods=['GET'])
def adicionar_form():
    return render_template('adicionar.html')

# SALVAR NOVO FILME
@views.route('/adicionar', methods=['POST'])
def adicionar_filme():
    titulo = request.form.get('titulo', '').strip()
    ano = request.form.get('ano', '').strip()
    descricao = request.form.get('descricao', '').strip()
    foto = request.files.get('foto')

    if not titulo or not ano:
        flash("Título e ano são obrigatórios.")
        return redirect(url_for('views.adicionar_form'))

    try:
        ano_int = int(ano)
    except ValueError:
        flash("Ano inválido.")
        return redirect(url_for('views.adicionar_form'))

    foto_base64 = None
    if foto and foto.filename:
        foto_bytes = foto.read()
        base64_str = base64.b64encode(foto_bytes).decode('utf-8')
        foto_base64 = f"data:{foto.mimetype};base64,{base64_str}"

    novo = Filme(
        titulo=titulo,
        ano=ano_int,
        descricao=descricao,
        foto_base64=foto_base64
    )

    db.session.add(novo)
    db.session.commit()

    return redirect(url_for('views.listar_filmes'))

# FORMULÁRIO EDITAR
@views.route('/editar/<int:id>', methods=['GET'])
def editar_form(id):
    filme = Filme.query.get_or_404(id)
    return render_template('editar.html', filme=filme)

# SALVAR EDIÇÃO
@views.route('/editar/<int:id>', methods=['POST'])
def editar_filme(id):
    filme = Filme.query.get_or_404(id)

    titulo = request.form.get('titulo', '').strip()
    ano = request.form.get('ano', '').strip()
    descricao = request.form.get('descricao', '').strip()
    foto = request.files.get('foto')

    if not titulo or not ano:
        flash("Título e ano são obrigatórios.")
        return redirect(url_for('views.editar_form', id=id))

    try:
        ano_int = int(ano)
    except ValueError:
        flash("Ano inválido.")
        return redirect(url_for('views.editar_form', id=id))

    filme.titulo = titulo
    filme.ano = ano_int
    filme.descricao = descricao

    if foto and foto.filename:
        foto_bytes = foto.read()
        base64_str = base64.b64encode(foto_bytes).decode('utf-8')
        filme.foto_base64 = f"data:{foto.mimetype};base64,{base64_str}"

    db.session.commit()
    return redirect(url_for('views.listar_filmes'))

# APAGAR FILME
@views.route('/apagar/<int:id>', methods=['GET', 'POST'])
def apagar_filme(id):
    filme = Filme.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(filme)
        db.session.commit()
        return redirect(url_for('views.listar_filmes'))
    return render_template('apagar.html', filme=filme)

# PÁGINA DE CONFIRMAÇÃO
@views.route('/apagar/confirmar/<int:id>')
def apagar_confirmar(id):
    filme = Filme.query.get_or_404(id)
    return render_template('apagar_confirmar.html', filme=filme)
