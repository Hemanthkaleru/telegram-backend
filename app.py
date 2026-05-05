from flask import Flask, request, jsonify
import requests
import os

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

    user = data.get("user", "User")
    message = data.get("message", "")
    reply = data.get("reply", "")

    text = f"👤 {user}\n💬 {message}\n🤖 {reply}"

    # 🔴 Safety check
    if not BOT_TOKEN or not CHAT_ID:
        return jsonify({"error": "Missing BOT_TOKEN or CHAT_ID"}), 500

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        res = requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": text
        }, timeout=5)   # ✅ timeout added

        print("Telegram response:", res.text)

        return jsonify({
            "status": "sent",
            "telegram_response": res.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500