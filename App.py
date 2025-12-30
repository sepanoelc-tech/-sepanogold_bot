from flask import Flask, request
import requests
import os

TOKEN = os.environ.get("8513697486:AAFbeub9lQ9AbQ0g5yP_RlItQMJ7082Mn1M")
CHAT_ID = os.environ.get("@sepanogold")

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    signal = data.get("message", "سیگنال جدید")
    price = data.get("price", "نامشخص")
    time  = data.get("time", "نامشخص")

    text = f"""
🚨 سیگنال قوی طلا (XAUUSD)

📌 نوع: {signal}
⏰ زمان: {time}
💰 قیمت: {price}
⏱ تایم‌فریم: 1 دقیقه

⚠️ فقط سیگنال – مدیریت ریسک با شما
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return "ok"

app.run(host="0.0.0.0", port=10000)
