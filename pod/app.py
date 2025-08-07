from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def index():
    return "OK", 200

@app.route("/healthz")
def health():
    # Simulate failure after 30 seconds
    if time.time() - start_time > 30:
        return "Unhealthy", 500
    return "Healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)