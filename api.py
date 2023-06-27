from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
app = Flask(__name__)
CORS(app)

@app.route('/api/events', methods=['GET'])
def get_events():
    events = [
        {
            'id': 1,
            'datetime': datetime.today(),
            'description': 'Event 1',
            "imageURL": "event1.jpg"
        },
        {
            'id': 2,
            'date': datetime(2023, 7, 28),
            'description': 'Event 2',
            "imageURL": "event1.jpg"
        },
        {
            'id': 3,
            'date': datetime(2023, 8, 23),
            'description': 'Event 3',
            "imageURL": "event1.jpg"
            
        }
        #... Add more events as needed
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
