from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


# 普通に必須パラメータも指定できる
async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        # 普通に例外送出もできる
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


"""
ただDependencyを実行したいだけで、戻り値を必要としないときデコレータに書くことができる
普通に必須パラメータも指定できる
普通に例外送出もできる
"""
