import dotenv
from openai import OpenAI

from pydantic import BaseModel, Field, EmailStr

dotenv.load_dotenv()


class UserInfo(BaseModel):
    """传递用户的信息进行数据提取&处理，涵盖 name、age、email 等"""
    name: str = Field(..., description="用户名字")
    age: int = Field(..., gt=0, description="用户年龄，必须为正整数")
    email: EmailStr = Field(..., description="用户电子邮箱")


client = OpenAI()

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    extra_body={
        "thinking": {"type": "disabled"}
    },  # deepseek-v4-flash 推理模型(思考模式)不支持工具调用 直接使用聊天模型
    messages=[
        {"role": "user", "content": "用户名小明，年龄18，联系方式xiaoming@163.com"}
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": UserInfo.__name__,
                "description": UserInfo.__doc__,
                "parameters": UserInfo.model_json_schema()
            }
        }
    ],
    tool_choice={"type": "function", "function": {"name": UserInfo.__name__}}
)

tool_args = response.choices[0].message.tool_calls[0].function.arguments

user_info = UserInfo.model_validate_json(tool_args)
print(user_info)
