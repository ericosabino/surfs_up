from flask import Flask

app = Flask(__name__)


# Also knows as the route
@app.route('/')

def hello_world():
    return 'Hello world'