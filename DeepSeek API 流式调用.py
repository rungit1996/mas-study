import os

import dotenv
import requests

dotenv.load_dotenv()
with requests.request(
        method="POST",
        url="https://api.deepseek.com/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}"
        },
        json={
            "model": "deepseek-v4-flash",
            "messages": [
                {"role": "user", "content": "你好，你是谁？"}
            ],
            "thinking": {
                "type": "disabled"
            },
            "stream": True
        }
) as resp:
    for line in resp.iter_lines(decode_unicode=True):
        if line:
            if line.startswith("data:"):
                data = line.lstrip("data:").strip()
                print("data:", data)
