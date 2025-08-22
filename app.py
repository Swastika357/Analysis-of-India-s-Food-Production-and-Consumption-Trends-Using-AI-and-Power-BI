from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to send requests

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        avg_production = float(data['avg_production'])
        std_production = float(data['std_production'])
        cagr = float(data['CAGR'])

        # Simulated prediction logic for demo purposes
        if avg_production > 2500:
            predicted_item = "Rice"
            confidence = 0.95
        elif avg_production > 1500:
            predicted_item = "Wheat"
            confidence = 0.88
        elif avg_production > 800:
            predicted_item = "Maize"
            confidence = 0.84
        else:
            predicted_item = "Barley"
            confidence = 0.79

        # Create dummy probability list (length = 94 crops)
        dummy_probs = [0.0] * 94
        dummy_probs[0] = round(confidence, 2)

        return jsonify({
            'predicted_crop': predicted_item,
            'probabilities': dummy_probs
        })

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def home():
    return "Flask app is running!"

if __name__ == '__main__':
    app.run(debug=True)
