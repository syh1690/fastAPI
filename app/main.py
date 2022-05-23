from typing import Optional

from fastapi import FastAPI

import json
data = json.load(open('./sampledata.json', 'r'))

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fpl/events/{week}")
def read_profile_page(week: int):
    return data["events"][week-1]

@app.get("/fpl/events/highest_score/{week}")
def read_profile_page(week: int):
    return data["events"][week-1]["highest_score"]    