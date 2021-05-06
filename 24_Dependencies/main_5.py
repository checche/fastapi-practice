from fastapi import Depends, FastAPI, Header, HTTPException


# 普通に必須パラメータも指定できる
async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        # 普通に例外送出もできる
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


@app.get("/users/")
async def read_users():
    return [{"item": "Foo"}, {"item": "Bar"}]


"""
アプリ全体にDIできる
"""
