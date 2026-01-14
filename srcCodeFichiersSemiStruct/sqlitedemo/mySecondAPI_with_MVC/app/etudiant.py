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


# ----------------- Modèle User pour JWT -----------------
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # mot de passe hashé

    def __repr__(self):
        return f"<User {self.username}>"
