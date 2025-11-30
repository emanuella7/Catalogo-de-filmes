from app import db

class Filme(db.Model):
    __tablename__ = 'filmes'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    foto_base64 = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Filme {self.titulo}>"
