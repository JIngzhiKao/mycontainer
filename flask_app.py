from flask import Flask
import rhino3dm as rhino
from flask import flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from test01!'

@app.route('/test')
def Linkstart():
    return 'Link Start!'

@app.route('/news')   #增加一个news页面
def newspage():
    newinformation="code 2120 assessment1！"
    return render_template("news.html",data=newinformation)

app.route('/product')  #增加一个product页面
def productpage():    
    return render_template("product.html")


