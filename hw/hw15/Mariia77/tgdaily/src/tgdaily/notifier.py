import requests
import json

CONFIG_PATH = "../../config.json"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def send_message(text):
    config = load_config()
    token = config["token"]
    chat_id = config["chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"❌ Ошибка отправки: {response.text}")
    else:
        print("📤 Сообщение отправлено в Telegram")
