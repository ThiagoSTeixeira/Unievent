from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/events', methods=['GET'])
def get_events():
    events = [
        {
            'id': 1,
            'date': '2023-06-10',
            'description': 'Event 1'
        },
        {
            'id': 2,
            'date': '2023-06-12',
            'description': 'Event 2'
        },
        {
            'id': 3,
            'date': '2023-06-14',
            'description': 'Event 3'
        }
        #... Add more events as needed
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
