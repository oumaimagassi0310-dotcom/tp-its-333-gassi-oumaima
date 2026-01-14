from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
DATA_FILE = 'data.json'
PERSON_SERVICE_URL = 'http://localhost:5001/persons'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def check_person_exists(person_id):
    resp = requests.get(f'{PERSON_SERVICE_URL}/{person_id}')
    return resp.status_code == 200

@app.route('/health/<int:person_id>', methods=['GET'])
def get_health(person_id):
    if not check_person_exists(person_id):
        return jsonify({'error': 'Person not found'}), 404
    data = load_data()
    return jsonify(data.get(str(person_id), {}))

@app.route('/health/<int:person_id>', methods=['POST', 'PUT'])
def add_update_health(person_id):
    if not check_person_exists(person_id):
        return jsonify({'error': 'Person not found'}), 404
    new_data = request.json
    data = load_data()
    data[str(person_id)] = new_data
    save_data(data)
    return jsonify({'message': 'Health data saved'})

@app.route('/health/<int:person_id>', methods=['DELETE'])
def delete_health(person_id):
    if not check_person_exists(person_id):
        return jsonify({'error': 'Person not found'}), 404
    data = load_data()
    if str(person_id) in data:
        del data[str(person_id)]
        save_data(data)
        return jsonify({'message': 'Deleted'})
    return jsonify({'error': 'No health data found'}), 404

@app.route('/', methods=['GET'])
def home():
    return "Health Service is running!"

if __name__ == '__main__':
    app.run(port=5002, debug=True)
