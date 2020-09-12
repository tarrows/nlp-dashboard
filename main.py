from fastapi import FastAPI
from tortoise import Tortoise
from lib import models

app = FastAPI()
db_url = 'sqlite://db.sqlite3'
modules = {'models': ['lib.models']}


@app.get('/')
async def index():
    await Tortoise.init(db_url=db_url, modules=modules)
    stories = await models.Story.all()
    await Tortoise.close_connections()
    return {"stories": list(stories)}


@app.get('/stories')
async def stories():
    stories = await models.Story.all()
    return stories


@app.get('/stories/{id}')
async def story(id: int):
    story = await models.Story.get_or_none(id=id)
    return story
