from flask import Flask
import rhino3dm as rhino

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from test01!'

@app.route('/test')
def Linkstart():
    return 'Link Start!'




