#Python Flask Application
# - JSON Response
# - Port 8080
# - using flask, jsonify, and request modules 

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def ReturnJSON():
    
    # JSON Response 
    if (request.method == 'GET'):
        data = {
            "message": "Automate all the things!",
            "timestamp": 1529729125
        }
        return jsonify(data)


# Declaring 0.0.0.0 and Port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
