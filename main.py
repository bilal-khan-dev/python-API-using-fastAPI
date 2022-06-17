from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    is_published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "My first fastAPI"}


@app.post("/createposts")
async def create_posts(post: Post):    
    return {"data": post.dict()}
