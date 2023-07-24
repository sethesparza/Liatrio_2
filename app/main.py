from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def ReturnJSON():
    if (request.method == 'GET'):
        data = {
            "message": "Automate all the things!",
            "timestamp": 1529729125
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    