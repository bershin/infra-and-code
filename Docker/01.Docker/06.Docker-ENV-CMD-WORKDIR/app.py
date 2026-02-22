from flask import Flask, render_template
import os

environment = os.getenv('APP_ENVIRONMENT', 'dev')

app = Flask(__name__)

@app.route('/')
def index():
    if environment=='dev':
        return render_template('dev.html')
    elif environment=='qa':
        return render_template('qa.html')
    else:
        return "<h1>Unknown environment</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)