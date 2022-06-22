import rhino3dm as rhino
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# main


@app.route('/')
def index():
    return render_template('index.html')


# api
@app.route('/api', methods=['POST'])
def api():
    name = request.form['name']
    length = request.form['length']
    width = request.form['width']
    height = request.form['height']
   
 
    
    msg = f'Name:{name} Length:{length} WIdth:{width} Height:{height}'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run(debug=False)




