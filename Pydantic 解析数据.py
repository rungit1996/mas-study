from pydantic import BaseModel, Field, EmailStr


class UserInfo(BaseModel):
    """传递用户的信息进行数据提取&处理，涵盖 name、age、email 等"""
    name: str = Field(..., description="用户名字")
    age: int = Field(..., gt=0, description="用户年龄，必须是正整数")
    email: EmailStr = Field(..., description="用户的电子邮件")


# 模拟从 Tool Calls 的 arguments 中获取的字符串
json_string = '{"name": "张三", "age": 22, "email": "zhangsan@example.com"}'

# --- Pydantic 的优雅之道 ---
try:
    user = UserInfo.model_validate_json(json_string)  # Pydantic V2 的推荐方法

    # 得到的是一个真正的 Python 对象，而不是字典
    print(f"解析成功！用户名：{user.name}")
    print(f"用户年龄：{user.age}")
    print(f"用户邮箱：{user.email}")
    print(user)  # 打印出的对象清晰明了

except Exception as e:
    print(f"数据校验失败：{e}")

# 试试错误数据
invalid_json_string = '{"name": "李四", "age": -22, "email": "lisi#example.com"}'

try:
    user = UserInfo.model_validate_json(invalid_json_string)
    print(f"解析成功！用户名：{user.name}")
    print(f"用户年龄：{user.age}")
    print(f"用户邮箱：{user.email}")
    print(user)
except Exception as e:
    print("\n--- 错误数据测试 ---")
    print(f"数据校验失败：\n{e}")
