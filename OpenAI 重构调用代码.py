import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(api_key="sk-8985ce947fbf47e080e18e616a118a07", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "你好，你是谁？"}
    ]
)

print("推理内容：", response.choices[0].message.reasoning_content)
print("返回结果：", response.choices[0].message.content)
