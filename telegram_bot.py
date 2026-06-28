import requests
from config import BOT_TOKEN, CHANNEL_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": CHANNEL_ID,
            "text": text
        }
    )

    return response.json()

def send_photo(photo_path, caption=""):

    url = f"{BASE_URL}/sendPhoto"

    with open(photo_path, "rb") as photo:

        response = requests.post(
            url,
            data={
                "chat_id": CHANNEL_ID,
                "caption": caption
            },
            files={
                "photo": photo
            }
        )

    return response.json()