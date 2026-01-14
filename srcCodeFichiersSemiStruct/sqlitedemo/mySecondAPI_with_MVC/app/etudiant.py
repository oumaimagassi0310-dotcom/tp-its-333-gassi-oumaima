from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Etudiant(db.Model):
    __tablename__ = 'etudiants'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(20))

    def __repr__(self):
        return f"<Etudiant {self.nom}>"
