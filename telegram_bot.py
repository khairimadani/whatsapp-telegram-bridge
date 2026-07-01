import requests
from config import BOT_TOKEN, CHANNEL_ID, GROUP_ID, GROUP_TOPIC_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(text):

    url = f"{BASE_URL}/sendMessage"

    # Channel
    requests.post(
        url,
        json={
            "chat_id": CHANNEL_ID,
            "text": text
        }
    )

    # DATEK topic
    requests.post(
        url,
        json={
            "chat_id": GROUP_ID,
            "message_thread_id": GROUP_TOPIC_ID,
            "text": text
        }
    )


def send_photo(photo_path, caption=""):

    url = f"{BASE_URL}/sendPhoto"

    # Channel
    with open(photo_path, "rb") as photo:
        requests.post(
            url,
            data={
                "chat_id": CHANNEL_ID,
                "caption": caption
            },
            files={
                "photo": photo
            }
        )

    # DATEK topic
    with open(photo_path, "rb") as photo:
        requests.post(
            url,
            data={
                "chat_id": GROUP_ID,
                "message_thread_id": GROUP_TOPIC_ID,
                "caption": caption
            },
            files={
                "photo": photo
            }
        )