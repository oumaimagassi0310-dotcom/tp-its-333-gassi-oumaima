## EXO1: API GET: renvoyer un helloworld - API end point name: "api/salutation"

## EXO2: API POST: renvoyer un nom fourni en parametre - API end point name: "api/utilisateurs"

# to be tested with curl: 
# >> curl -i -X GET http://localhost:5000/api/salutation
# >> curl -i -X POST -H 'Content-Type: application/json' -d '{"nom": "Bob"}' http://localhost:5000/api/utilisateurs



from flask import Flask, jsonify, request

app = Flask(__name__)

# EXO1: API GET
#@app.route('/api/salutation', methods=['GET'])
#def salutation():
    #return jsonify({"message": "Hello World"})



# EXO2: API POST
@app.route('/api/utilisateurs', methods=['POST'])
def utilisateurs():
    data = request.get_json()
    
    if not data or 'nom' not in data:
        return jsonify({"error": "Le champ 'nom' est requis"}), 400

    return jsonify({"nom": data['nom']}), 201

if __name__ == '__main__':
    app.run(debug=True)