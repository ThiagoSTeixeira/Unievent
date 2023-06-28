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
            'title': 'SheHacks!',
            "imageURL": "shehacks.png",
            "description": "Junte-se a um time multidisciplinar de mulheres universitárias cis e trans para propor formas de melhorar a acessibilidade tecnológica na sociedade",
            "owner": "USPCodeLab",
            "ownerImageURL": "uspcodelab.png"
        },
        {
            'id': 2,
            'date': datetime(2023, 7, 28),
            'title': 'BixeCamp 2023.2',
            "imageURL": "maratonusp.jpg",
            "description": "Aulas introdutórias sobre programação competitiva",
            "owner": "MaratonUSP",
            "ownerImageURL": "maratonusp.png"
        },
        {
            'id': 3,
            'date': datetime(2023, 8, 23),
            'title': 'Event 3',
            "imageURL": "event1.jpg",
            "description": "this is a test description for this event, blabla",
            "owner": "IMESec",
            "ownerImageURL": "imesec.jpg"
            
        }
        #... Add more events as needed
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
