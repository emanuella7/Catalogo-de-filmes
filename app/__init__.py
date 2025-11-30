import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Configurações
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # banco relativo à raiz do projeto (WEB/filmes.db)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'filmes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(base_dir, '..', 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)

    # Importar modelos (para registro do SQLAlchemy)
    with app.app_context():
        from app.models.Filme import Filme  # importa o modelo
        db.create_all()

    # Registrar rotas definidas em controllers usando app.route
    from app.controllers import views
    views.register_routes(app)

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'secret'

    db.init_app(app)

    from app.controllers.views import views
    app.register_blueprint(views)

    with app.app_context():
        db.create_all()
    return app
