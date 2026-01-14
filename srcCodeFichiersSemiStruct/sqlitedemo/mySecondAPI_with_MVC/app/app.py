from flask import Flask, render_template, request
from etudiants import insert_etudiant, get_etudiants, create_table

app = Flask(__name__)

# Créer la table au démarrage
create_table()

@app.route("/")
def index():
    students = get_etudiants()
    return render_template("list.html", etudiants=students)

@app.route("/new")
def new_student_form():
    return render_template("new.html")

@app.route("/new", methods=["POST"])
def add_student():
    nom = request.form["nom"]
    addr = request.form["addr"]
    pin = request.form["pin"]

    insert_etudiant(nom, addr, pin)

    return "Étudiant ajouté avec succès ! <br><a href='/'>Retour</a>"

if __name__ == "__main__":
    app.run(debug=True)
