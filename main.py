from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel


app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/')
async def read_items(
    q: Optional[list[str]] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results


@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result


@app.get('/items/{item_id}')
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    return item


@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    # ModelNameのメンバとの比較
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    # 実際の値の取得
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
