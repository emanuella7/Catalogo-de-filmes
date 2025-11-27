from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar as rotas
    from app.controllers.views import views
    app.register_blueprint(views)

    return app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    diretor = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()
