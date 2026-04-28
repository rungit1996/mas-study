# -------------- Pydantic V2 实用技巧 ----------------

from pydantic import BaseModel, field_validator, EmailStr, computed_field, Field


class User(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def name_must_not_be_admin(cls, value: str) -> str:
        if "admin" in value.lower():
            raise ValueError("用户名不能包含'admin'")
        return value.title()  # 顺便还可以对数据进行清洗，比如首字母大写


# test
# user = User(name="test_admin")  # 这会直接抛出 ValueError
user_ok = User(name="jason")
print(user_ok.name)  # 输出：Jason


# ---------- 甚至可以基于已有字段，计算出新字段 ----------

class UserWithUsername(BaseModel):
    name: str
    email: EmailStr

    @computed_field
    @property
    def username(self) -> str:
        # 从邮箱中提取用户名
        return self.email.split("@")[0]


user2 = UserWithUsername(name="张三", email="zhangsan@example.com")
print(user2.username)  # 输出 zhangsan
print(user2.model_dump())  # dump 出来的 json 也会包含这个衍生字段


# ---------- 导出模型在 API 响应场景使用频率很高 ----------
class UserInfo(BaseModel):
    name: str
    age: int
    email: EmailStr


user3 = UserInfo(name="张三", age=22, email="zhangsan@example.com")
user3_dict = user3.model_dump()  # 导出为字典
print(user3_dict)

user3_json = user3.model_dump_json()  # 导出为 JSON 字符串
print(user3_json)

# 从字典/JSON创建模型（model_validate、model_validate_json），常用于从接口、数据库中的数据快速创建 Python 对象
data_dict = {"name": "张三", "age": 11, "email": "zhangsan@example.com"}
json_str = '{"name": "李四", "age": 12, "email": "lisi@example.com"}'
user4 = UserInfo.model_validate(data_dict)
user5 = UserInfo.model_validate_json(json_str)
print(user4)
print(user5)


# ---------- 快速将 BaseModel 的属性生成符合 OpenAI Tool Calls 格式的工具参数声明，这是 AI 应用开发框架 LangChain 目前的做法

class UserInfo2(BaseModel):
    """传递用户的信息进行数据提取&处理，涵盖 name、age、email 等"""
    name: str = Field(..., description="用户名字")
    age: int = Field(..., gt=0, description="用户年龄，必须是正整数")
    email: EmailStr = Field(..., description="用户电子邮箱")


tools = [
    {
        "type": "function",
        "function": {
            "name": UserInfo2.__name__,
            "description": UserInfo2.__doc__,
            "parameters": UserInfo2.model_json_schema()
        }
    }
]
