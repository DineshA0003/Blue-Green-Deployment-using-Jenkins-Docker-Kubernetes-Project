from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "Blue Version 1")

@app.route("/")
def home():
    return jsonify({
        "message": "Blue Green Deployment Project",
        "version": VERSION,
        "status": "Application Running Successfully"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "version": VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

