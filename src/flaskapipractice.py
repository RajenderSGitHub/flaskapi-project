from flask import Flask, jsonify, request
from datetime import datetime

"""
Flask object instatite 
Define the routing 
defein GET method and return the output in json format 
"""

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Greetings")

@app.route('/healthstatus', methods=['GET'])
def healthstatus():
    return jsonify('Health check status good')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    if request.method == 'POST':

        # name = request.args.get('name')
        data = request.json
        name = data.get('name')
        text = {'message':f'Hello {name}', 'Time':f'Current timestamp is {datetime.now()}'}

    elif request.method == 'GET':
        name = request.args.get('name')
        text = {'message':f'Hello {name}', 'Time':f'Current timestamp is {datetime.now()}'}

    return jsonify(text)

if __name__ == '__main__':
    app.run()