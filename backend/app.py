from flask import Flask, request, jsonify, send_from_directory
import joblib
import os

# Flask app
app = Flask(__name__, static_folder="../frontend", static_url_path="")

# Paths to models
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "model.pkl")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "models", "vectorizer.pkl")

# Load trained model and vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model and vectorizer loaded successfully")
except Exception as e:
    raise RuntimeError(f"Error loading model/vectorizer: {e}")

# Serve frontend
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

# Predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    message = data.get("message")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    X = vectorizer.transform([message])
    prediction = model.predict(X)[0]

    return jsonify({"prediction": "spam" if prediction == 1 else "not spam"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
