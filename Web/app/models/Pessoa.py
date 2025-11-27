from app import db

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    diretor = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f"<Filme {self.titulo} ({self.ano})>"
