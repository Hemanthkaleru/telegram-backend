from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/send", methods=["POST"])
def send():
    data = request.json

    text = f"👤 {data['user']}\n💬 {data['message']}\n🤖 {data['reply']}"

    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": text
        }, timeout=5)

        return jsonify({"status": "sent"})

    except Exception as e:
        return jsonify({"error": str(e)})