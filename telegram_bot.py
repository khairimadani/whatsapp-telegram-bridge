import requests
from config import BOT_TOKEN, CHANNEL_ID, GROUP_ID
CHAT_IDS = [CHANNEL_ID, GROUP_ID]

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    last_response = None

    for chat_id in CHAT_IDS:
        last_response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": text
            }
        )

    return last_response.json() if last_response else None

def send_photo(photo_path, caption=""):

    url = f"{BASE_URL}/sendPhoto"

    last_response = None

    for chat_id in CHAT_IDS:

        with open(photo_path, "rb") as photo:

            last_response = requests.post(
                url,
                data={
                    "chat_id": chat_id,
                    "caption": caption
                },
                files={
                    "photo": photo
                }
            )

    return last_response.json() if last_response else None