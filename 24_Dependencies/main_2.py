from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


@app.get("/items2/")
async def read_items2(commons: CommonQueryParams = Depends()):  # このように書くことができる
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


"""
- Dependency は Callable
- 依存関数の引数やクラスのコンストラクタ引数は、パスオペレーション関数と同様に処理される。
- クラスの場合インスタンスが注入される
- commons: CommonQueryParams = Depends()というふうに記述することができる
"""
