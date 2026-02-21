from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return jsonify(message=f"Resource ID: {id} is updated")

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
     return jsonify(message=f"Resource ID: {id} is deleted")
if __name__ == '__main__':
    app.run(debug=True)

# $ curl -X PUT http://127.0.0.1:5000/update/2345
# $ curl -X DELETE http://127.0.0.1:5000/delete/2345