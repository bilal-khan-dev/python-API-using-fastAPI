from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
    return {"message": "My first fastAPI"}


@app.post("/createposts")
async def create_posts(new_post: Post):
    return {"data": new_post}
