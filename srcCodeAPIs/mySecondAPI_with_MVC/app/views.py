from app import app
from flask import render_template, request, jsonify

### EXO1 - simple API
@app.route('/api/salutation', methods=['GET'])
def salutation():
    #return jsonify({"message": "Hello World"})


### EXO2 - API with simple display
@app.route('/route2')
def index2():
    message = "Hello world"
    return render_template ('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)

### EXO3 - API with parameters display
@app.route('/route3')
def index3():
    user={'name':'Oumaima', 'surname':'gassi'}
    return render_template('index.html', title='MDM', utilisateur=user) 

### EXO4 - API with parameters retrieved from URL 
@app.route('/route4')
def index4():
    name = request.args.get('name', 'Oumaima')
    surname = request.args.get('surname', 'Gassi')
    user = {'name': name, 'surname':surname}

    return render_template('index.html', title='MDM', utilisateur=user)
