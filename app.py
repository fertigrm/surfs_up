from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dog')
def hello_dog():
    return 'Hello Dog'