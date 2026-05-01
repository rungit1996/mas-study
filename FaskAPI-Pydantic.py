from typing import Optional

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=10, description="商品名称，3-10个字符")
    price: float = Field(..., gt=0, description="价格必须大于0")
    in_stock: bool


@app.post("/users/{user_id}/items")
async def create_item(
        user_id: int = Path(..., ge=1, description="用户ID必须>=1"),
        q: Optional[str] = Query(None, min_length=3, description="搜索关键字，最少3个字符"),
        item: Item = ...
):
    return {"user_id": user_id, "query": q, "item": item}
