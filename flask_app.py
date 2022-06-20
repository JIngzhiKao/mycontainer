from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from test!'

@app.route('/test')
def Linkstart():
    return 'Link Start!'
