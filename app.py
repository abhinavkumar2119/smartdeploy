from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "SmartDeploy App Running!"


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})


@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True)
