from fastapi import FastAPI

# 启动 API 服务
# app 是实例的名称 app = FastAPI()
# uvicorn FastAPI-Demo:app --reload

# 创建一个FastAPI实例，这个app对象就是我们所有API交互的核心
app = FastAPI()


# 创建一个“路径操作” (Path Operation)，@app.get("/") 是一个“装饰器”，它告诉FastAPI：
# 当有HTTP GET请求访问根路径("/")时，就执行下面的函数 root()
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


# 路径参数 (Path Parameters) 路径中的 {app_id} 会被作为参数传入函数
# http://127.0.0.1:8000/apps/9527?q=1234
@app.get("/apps/{app_id}")
async def get_app(app_id: int, q: str | None = None):
    return {"app_id": app_id, "q": q}
