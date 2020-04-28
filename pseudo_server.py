from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def login():
    if not request.json:
        return jsonify({'status': 'failed'}), 400
    userlogin = {
        'username': request.json['username'],
        'password': request.json['password']
    }

    # insert code to check database if username and password is correct

    return jsonify({'userlogin': userlogin}), 201


if __name__ == '__main__':
    app.run(debug=True, port='3200')



