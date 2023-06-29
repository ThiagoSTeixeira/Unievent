from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/authenticate', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        return jsonify({'message': 'Logged in successfully'}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/events', methods=['GET'])
def get_events():
    with open('events.json', 'r') as file:
        events = json.load(file)
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
