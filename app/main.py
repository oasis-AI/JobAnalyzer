from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {
        "item_id": item_id,
        "q": q,
        "Hello": "World",
        "item_id_type": type(item_id),
        "q_type": type(q),
        "item_id_q": item_id + int(q) if q else item_id,
    }
