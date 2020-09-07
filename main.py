from fastapi import FastAPI
from lib import models

app = FastAPI()


@app.get('/')
async def index():
    stories = await models.Story.all()
    return {"stories": list(stories)}
