from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return jsonify(message=f"Resource {id} updated")

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(message=f"Resource {id} deleted")


if __name__ == '__main__':
    app.run(debug=True)