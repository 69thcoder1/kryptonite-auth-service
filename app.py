from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Kryptonite Auth Service",
        "status": "running",
        "environment": "production"
    })

@app.route("/auth")
def auth():
    return jsonify({
        "service": "authentication",
        "status": "ready"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
