from flask import Flask, request, jsonify
import requests
import os

# ✅ CREATE APP FIRST
app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


@app.route("/")
def home():
    return "Backend running"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/send", methods=["POST"])
def send():
    data = request.json

    text = f"👤 {data['user']}\n💬 {data['message']}\n🤖 {data['reply']}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    res = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    print("Telegram response:", res.text)

    return jsonify({
        "status": "sent",
        "telegram_response": res.text
    })