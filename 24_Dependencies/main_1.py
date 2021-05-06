from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(
    commons: dict = Depends(common_parameters),
):  # Dependsを引数に書くだけで実行してくれる
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


"""
- OpenAPIに自動的に統合される
- パスオペレーション関数(ex. read_items)の実行前にDependenciesを実行し、
  その結果をパスオペレーション関数に注入できる
- DependenciesにDependenciesを注入することでパーミッションをいい感じにしたりもできる
"""
