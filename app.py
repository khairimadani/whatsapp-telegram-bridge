from flask import Flask, request
from telegram_bot import send_message, send_photo
from whatsapp_api import download_media

app = Flask(__name__)

VERIFY_TOKEN = "datekin123"

@app.route("/")
def home():
    return "WhatsApp Bridge Running!"

@app.route("/webhook", methods=["GET"])
def verify():
    ...
    
@app.route("/webhook", methods=["POST"])
def webhook():
    ...