import requests
from config import BOT_TOKEN, CHANNEL_ID, GROUP_ID, GROUP_TOPIC_ID

CHAT_IDS = [CHANNEL_ID, GROUP_ID]

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text):
    url = f"{BASE_URL}/sendMessage"

    for chat_id in CHAT_IDS:

        payload = {
            "chat_id": chat_id,
            "text": text
        }

        # Only add topic when sending to the group
        if chat_id == GROUP_ID:
            payload["message_thread_id"] = GROUP_TOPIC_ID

        requests.post(url, json=payload)


def send_photo(photo_path, caption=""):
    url = f"{BASE_URL}/sendPhoto"

    for chat_id in CHAT_IDS:

        payload = {
            "chat_id": chat_id,
            "caption": caption
        }

        if chat_id == GROUP_ID:
            payload["message_thread_id"] = GROUP_TOPIC_ID

        with open(photo_path, "rb") as photo:
            requests.post(
                url,
                data=payload,
                files={
                    "photo": photo
                }
            )