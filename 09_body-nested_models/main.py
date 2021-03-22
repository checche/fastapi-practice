from enum import Enum
from typing import Optional

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, HttpUrl


app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: set[str] = set()
    image: Optional[list[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: list[Item]


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def read_items(
    *,
    item_id: int = Path(..., title='The ID of the item to get', ge=0, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5),
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    print(results)
    return results


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, 'item': item}
    return results


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


@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer


@app.post('/images/multiple/')
async def create_multiple_images(images: list[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
