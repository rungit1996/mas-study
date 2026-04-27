import base64

import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key="sk-6hW5iA9UMKnmK4W5Ibatqm6cdUCvyPBGiWOSe7EhQCJjatvE",
    base_url="https://api.moonshot.cn/v1"
)

image_path = "./resources/步步.jpg"

with open(image_path, "rb") as f:
    image_data = f.read()

image_url = f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"

response = client.chat.completions.create(
    model="moonshot-v1-8k-vision-preview",
    messages=[
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
)

print("返回结果：", response.choices[0].message.content)
