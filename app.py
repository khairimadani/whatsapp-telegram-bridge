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
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print(data)

    try:
        entry = data["entry"][0]
        change = entry["changes"][0]
        value = change["value"]

        if "messages" not in value:
            return "OK", 200

        message = value["messages"][0]
        sender = message["from"]

        if message["type"] == "text":
            text = message["text"]["body"]

            send_message(
                f"📩 WhatsApp\n\n"
                f"From: {sender}\n\n"
                f"{text}"
            )

        elif message["type"] == "image":
            media_id = message["image"]["id"]
            caption = message["image"].get("caption", "")
            photo = download_media(media_id)

            telegram_caption = (
                "📷 WhatsApp Photo\n\n"
                f"👤 From: {sender}\n\n"
    )

        if caption:
            telegram_caption += f"📝 Caption:\n{caption}"
            
        send_photo(photo, telegram_caption)

    except Exception as e:
        print("Error:", e)

    return "OK", 200