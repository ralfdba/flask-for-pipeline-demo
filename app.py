from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola Mundo from Python and Flask</p>"
