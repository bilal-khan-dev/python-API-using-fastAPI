from fastapi import FastAPI
from fastapi.params import Body 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "My first fastAPI"}

@app.post("/name")
async def name(payload: dict = Body(...)):
    return {
        "message" : payload
    }