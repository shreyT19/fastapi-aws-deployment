from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def read_items():
    return [{"name": "Item Foo"}, {"name": "Item Bar"}]

handler = Mangum(app=app)