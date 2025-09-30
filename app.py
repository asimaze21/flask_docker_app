from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my Flask app running in Docker!"

@app.route("/api/data")
def get_data():
    return jsonify({
        "message": "This is sample API data",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
