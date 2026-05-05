@app.route("/send", methods=["POST"])
def send():
    data = request.json

    text = f"👤 {data['user']}\n💬 {data['message']}\n🤖 {data['reply']}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    res = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    print("Telegram status:", res.status_code)
    print("Telegram response:", res.text)

    return {
        "status": "sent",
        "telegram_response": res.text
    }