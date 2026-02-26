from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Home!"

@app.route('/hello')
def hello():
    return jsonify(message="Hello to Flask!")

if __name__ == '__main__':
    app.run(debug=True)