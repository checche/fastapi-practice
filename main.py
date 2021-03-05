from enum import Enum
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


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
