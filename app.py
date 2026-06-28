from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Railway!"

@app.route("/webhook", methods=["GET"])
def verify():
    return "Webhook OK"

@app.route("/webhook", methods=["POST"])
def webhook():
    return "EVENT_RECEIVED", 200