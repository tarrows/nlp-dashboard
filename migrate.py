from tortoise import Tortoise, run_async


async def migrate():
    db_url = 'sqlite://db.sqlite3'
    modules = {'models': ['lib.models']}
    await Tortoise.init(db_url=db_url, modules=modules)
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(migrate())
