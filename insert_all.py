import json
from pathlib import Path
from tortoise import Tortoise, run_async
from lib import models


async def insert_all(db_url: str, modules: str, data: str):
    p = Path(data)
    assert p.is_dir()

    keys = [
        ('id', 0),
        ('title', ''),
        ('url', ''),
        ('score', 0),
        ('by', ''),
        ('time', 0),
    ]

    await Tortoise.init(db_url=db_url, modules=modules)

    for item in p.iterdir():
        if not item.suffix == '.json':
            continue

        with item.open() as f:
            story = json.load(f)
        record = {key: story.get(key, default) for (key, default) in keys}
        # try:
        await models.Story.create(**record)
        # except...

    await Tortoise.close_connections()

if __name__ == '__main__':
    db_url = 'sqlite://db.sqlite3'
    modules = {'models': ['lib.models']}
    data = './data'
    run_async(insert_all(db_url, modules, data))
