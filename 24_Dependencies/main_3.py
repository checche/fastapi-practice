from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_items(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


"""
- 連鎖的なDIが可能
- 1つのパス操作に対して全体を通して複数回同じDIが宣言されている場合
  通常はキャッシュを使って同じ結果を返すが
  Depends(get_value, use_cache=False)とすることで複数回の実行が可能
"""
