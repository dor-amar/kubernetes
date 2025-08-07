from flask import Flask
import sys

app = Flask(__name__)

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/kill")
def kill():
    sys.exit(1)  # This will crash the container with exit code 1

@app.route("/")
def home():
    return "Welcome to my web app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
