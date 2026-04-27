import base64
import os

import dotenv
import requests

dotenv.load_dotenv()

image_path = "./resources/自定义.jpg"

with open(image_path, "rb") as f:
    image_data = f.read()

image_url = f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"

response = requests.request(
    method="POST",
    url="https://api.moonshot.cn/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {os.getenv('MOONSHOT_API_KEY')}"
    },
    json={
        "model": "moonshot-v1-8k-vision-preview",
        "temperature": 0.3,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    },
                    {
                        "type": "text",
                        "text": "描述一下图中的情绪和故事感？"
                    }
                ]
            }
        ]
    }
)

print(response.json())
