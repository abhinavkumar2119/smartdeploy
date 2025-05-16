from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return jsonify(message="SmartDeploy App is running")

@app.route('/health')
def health():
    return jsonify(status="OK"), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    value = data.get("input")
    if value is None:
        logging.warning("No input provided")
        return jsonify(error="Missing input"), 400
    result = value * 2
    logging.info(f"Input: {value}, Result: {result}")
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
