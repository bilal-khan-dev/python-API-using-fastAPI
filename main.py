from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "My first fastAPI"}


@app.post("/createposts")
async def name(payload: dict = Body(...)):
    return {"new_posts": f"title {payload['title']} content: {payload['content']}"}
