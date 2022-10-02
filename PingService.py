from flask import Flask, jsonify, request
import requests, time
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

users = {
    "vcu": "rams",
}


def to_json(t):
    json_post = {
        'pingpong_t': t
    }
    return json_post

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class ValidationError(ValueError):
    pass

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Page Not Here'}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Something is Broke'}), 500

@app.route("/")
def PORT_FUNC():
    return 'go to 127.0.0.1:8000/ping'

@app.route('/ping', methods=['GET'])
@auth.login_required
def ping():
    start = time.time()*1000
    requests.get('http://127.0.0.1:7000/pong', auth=('vcu', 'rams'))
    end = time.time()*1000
    pingpong_t = end - start
    spingpong_t = str(pingpong_t)
    return jsonify({'pingpong_t': spingpong_t}), 201
