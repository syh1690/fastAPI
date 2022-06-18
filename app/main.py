from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import json

data = json.load(open('./sampledata.json', 'r'))

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("home.html",{"request": request})

@app.get("/resume",response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("resume.html",{"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fpl/events/{week}")
def read_profile_page(week: int):
    return data["events"][week-1]

@app.get("/fpl/events/highest_score/average_entry_score/{week}")
def read_profile_page(week: int):
    return [data["events"][week-1]["highest_score"],data["events"][week-1]["average_entry_score"]]