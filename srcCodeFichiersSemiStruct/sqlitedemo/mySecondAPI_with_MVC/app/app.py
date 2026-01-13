from flask import Flask, render_template, request
from srcCodeFichiersSemiStruct.sqlitedemo.mySecondAPI_with_MVC.app.etudiants import insert_etudiant

app = Flask(__name__)

@app.route("/new")
def new_student_form():
    return render_template("new.html")

@app.route("/new", methods=["POST"])
def add_student():
    nom = request.form["n"]
    addr = request.form["add"]
    pin = request.form["pin"]

    insert_etudiant(nom, addr, pin)

    return "Étudiant ajouté avec succès !"

if __name__ == "__main__":
    app.run(debug=True)
