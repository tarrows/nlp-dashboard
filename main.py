from fastapi import FastAPI
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from lib import models

app = FastAPI()
db_url = 'sqlite://db.sqlite3'
modules = {'models': ['lib.models']}


@app.get('/')
async def index():
    return {"hello": "world"}


@app.get('/stories')
async def stories():
    return await models.Story.all()


@app.get('/stories/{id}', responses={404: {"model": HTTPNotFoundError}})
async def story(id: int):
    return await models.Story.get(id=id)


register_tortoise(app, db_url=db_url, modules=modules, add_exception_handlers=True)
