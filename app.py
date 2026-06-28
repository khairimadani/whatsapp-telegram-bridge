from flask import Flask, request
from telegram_bot import send_message, send_photo
from whatsapp_api import download_media

app = Flask(__name__)

VERIFY_TOKEN = "datekin123"


@app.route("/")
def home():
    return "WhatsApp Bot is Running!"


@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()

    try:
        change = data["entry"][0]["changes"][0]["value"]

        if "messages" in change:

            message = change["messages"][0]
            sender = message["from"]

            if message["type"] == "text":

                text = message["text"]["body"]

                telegram_text = (
                    "📱 WhatsApp Message\n\n"
                    f"👤 From: {sender}\n\n"
                    f"💬 {text}"
                )

                send_message(telegram_text)

            elif message["type"] == "image":

                media_id = message["image"]["id"]

                caption = message["image"].get("caption", "")

                photo_path = download_media(media_id)

                telegram_caption = (
                    "📷 WhatsApp Photo\n\n"
                    f"👤 From: {sender}\n\n"
                    f"{caption}"
                )

                send_photo(photo_path, telegram_caption)

    except Exception as e:
        print("Error:", e)

    return "EVENT_RECEIVED", 200


import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )