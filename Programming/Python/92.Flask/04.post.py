from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route("/submit", methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    if name:
        return jsonify(mesage=f"My name is {name}")
    return jsonify(error="No new names"), 400

if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"name\": \"john\"}"
# curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"age\": \"john\"}"