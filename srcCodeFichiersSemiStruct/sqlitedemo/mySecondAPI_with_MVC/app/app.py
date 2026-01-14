from flask import Flask, render_template, request, redirect, url_for
from etudiant import db, Etudiant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "une_cle_secrete"

# Initialiser la DB avec Flask
db.init_app(app)

# Créer les tables si elles n'existent pas
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    etudiants = Etudiant.query.all()
    return render_template("list.html", etudiants=etudiants)

@app.route("/new")
def new_student_form():
    return render_template("new.html")

@app.route("/new", methods=["POST"])
def add_student():
    nom = request.form["nom"]
    addr = request.form["addr"]
    pin = request.form["pin"]

    if not nom.strip():
        return "Le nom est obligatoire ! <a href='/new'>Retour</a>"

    nouvel_etudiant = Etudiant(nom=nom, addr=addr, pin=pin)
    db.session.add(nouvel_etudiant)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
