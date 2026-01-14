from flask import Flask, render_template, request, redirect, url_for, jsonify
from etudiant import db, Etudiant, User  # On suppose que User est dans etudiant.py
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "une_cle_secrete"
app.config["JWT_SECRET_KEY"] = "une_autre_cle_secrete_pour_jwt"

# Initialiser DB et JWT
db.init_app(app)
jwt = JWTManager(app)

# Créer les tables si elles n'existent pas
with app.app_context():
    db.create_all()
    # Créer un utilisateur admin par défaut
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", password=generate_password_hash("password123"))
        db.session.add(admin)
        db.session.commit()

# ---------------- ROUTES ---------------- #

# Route pour la liste des étudiants (accessible sans auth)
@app.route("/")
def index():
    etudiants = Etudiant.query.all()
    return render_template("list.html", etudiants=etudiants)

# Formulaire pour ajouter un étudiant (accessible sans auth pour l'instant)
@app.route("/new")
def new_student_form():
    return render_template("new.html")

# Ajouter un étudiant (protégé par JWT)
@app.route("/new", methods=["POST"])
@jwt_required()
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

# Route pour se connecter et obtenir un token JWT
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Nom d'utilisateur ou mot de passe incorrect"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@app.route("/login", methods=["GET"])
def login_form():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
