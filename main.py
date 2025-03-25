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
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': [twit.to_dict() for twit in twits]})

@app.route('/twit', methods=['DELETE'])
def delete_twit():
    twit_json = request.get_json()
    body_to_delete = twit_json['body']
    author_to_delete = twit_json['author']
    
    new_twits = []
    found = False
    global twits
    
    for twit in twits:
        if twit.body == body_to_delete and twit.author == author_to_delete:
            found = True 
        else:
            new_twits.append(twit)  

    twits = new_twits
    
    if found:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'not found'})

@app.route('/twit', methods=['PUT'])
def change_twit():
    change_list = request.get_json()
    body_to_delete = change_list[0]['body']
    author_to_delete = change_list[0]['author']
    body_new = change_list[1]['body']
    author_new = change_list[1]['author']

    new_twits = []
    found = False
    global twits
    
    for twit in twits:
        if twit.body == body_to_delete and twit.author == author_to_delete:
            found = True
            new_twits.append(Twit(body_new, author_new))  
        else:
            new_twits.append(twit)  

    twits = new_twits
    
    if found:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'not found'})
    

    return 

if __name__ == "__main__":
    app.run(debug=True)
