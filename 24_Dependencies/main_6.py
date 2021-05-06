from fastapi import Depends, FastAPI, Header, HTTPException


class DBSession:
    def close(self):
        pass


async def get_db():
    db = DBSession()
    try:  # この依存関係を使ったパス操作やその他の依存関係からの例外を受け取ることができる
        yield db  # ここまで実行され、yieldした値が注入される
    # レスポンスのあとに以下が実行される
    finally:
        db.close()


"""
- yieldした値が注入される
  それ以降の処理はレスポンスのあとに実行される
- tryでこの依存関係を使ったパス操作やその他の依存関係からの例外を受け取ることができる
"""


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)


"""
こういう依存関係もyield以降の実行順序はうまくやってくれます。c->b->a
"""


"""
終了コード(yield以降のコード)は例外ハンドラのあとに実行される
例外処理があるなら、普通にtryブロックを書きましょう
"""
