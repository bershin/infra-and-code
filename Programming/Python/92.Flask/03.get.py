from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify(message="Welcome to flask!")

if __name__ == '__main__':
    app.run(debug=True)

# curl http://127.0.0.1:5000/greet