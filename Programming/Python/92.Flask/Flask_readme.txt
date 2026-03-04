python -m venv bjohnenv
source bjohnenv/bin/activate
pip install flask
python 01.Simple_flask.py


$ curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"name\": \"john\"}" -v
$ curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"age\": \"john\"}" -v

$ curl -X PUT http://127.0.0.1:5000/update/2345
$ curl -X DELETE http://127.0.0.1:5000/delete/2345