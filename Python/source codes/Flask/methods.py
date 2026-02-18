from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify(message="Hello, Welcome!")

from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get the JSON data from the request
    name = data.get('name')  # Extract the 'name' field from the JSON
    if name:  # Basic validation
        return jsonify(message=f"Hello, {name}!")
    return jsonify(error="No name provided"), 400

if __name__ == '__main__':
    app.run(debug=True)