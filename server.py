from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access from browser

@app.route('/applovin', methods=['GET'])
def get_applovin_report():
    api_key = request.args.get('api_key')
    start = request.args.get('start')
    end = request.args.get('end')
    columns = request.args.get('columns')

    if not all([api_key, start, end, columns]):
        return jsonify({"error": "Missing parameters"}), 400

    url = f"https://r.applovin.com/report?api_key={api_key}&start={start}&end={end}&columns={columns}&format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)