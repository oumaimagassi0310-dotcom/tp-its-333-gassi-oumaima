from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Créer la base de données dans le contexte Flask
with app.app_context():
    db.create_all()

# Routes CRUD
@app.route('/persons', methods=['POST'])
def create_person():
    data = request.json
    person = Person(name=data['name'])
    db.session.add(person)
    db.session.commit()
    return jsonify({'id': person.id, 'name': person.name}), 201

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person:
        return jsonify({'id': person.id, 'name': person.name})
    return jsonify({'error': 'Person not found'}), 404

@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Deleted'})
    return jsonify({'error': 'Person not found'}), 404

# Route GET simple pour vérifier le service
@app.route('/', methods=['GET'])
def home():
    return "Person Service is running!"

if __name__ == '__main__':
    app.run(port=5001, debug=True)
