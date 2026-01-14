from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = 'monsecret'

# Route GET simple pour tester dans le navigateur
@app.route('/', methods=['GET'])
def home():
    return "Auth Service is running!"

# Route POST pour générer un token
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password':
        token = jwt.encode(
            {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm='HS256'
        )
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(port=5000, debug=True)
