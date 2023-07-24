from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def ReturnJSON():
    if (request.method == 'GET'):
        data = {
            "message": "Automate all the things!",
            "timestamp": 1529729125
        }
        return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
