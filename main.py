from flask import Flask, json, jsonify, request

from model.twit import Twit

twits = []

app = Flask(__name__)

@app.route('/twit', methods=['POST'])
def create_twit():
    '''{"body": "Hello, World!", "author": "@philin"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    #aaa = json.dumps(twits)
    #print(aaa)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})

if __name__ == "__main__":
    app.run(debug=True)
