from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"message": "Aidan says hello from FastAPI on Google Cloud Run!"}
