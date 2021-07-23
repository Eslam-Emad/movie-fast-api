from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app =FastAPI()

@app.get("/movies")
def movies(status:Optional[str] = "da"):
    return {'status' : status}
    


class Movie(BaseModel):
    title:str
    decription:str


@app.post("/movies")
def add_movies(request:Movie):
    return request

