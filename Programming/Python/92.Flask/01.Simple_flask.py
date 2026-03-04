from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to flask microservice!"

if __name__ == '__main__':
    app.run(debug=True) 

# python 01.Simple_flask.py