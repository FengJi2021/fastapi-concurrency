import asyncio
import time
from fastapi import FastAPI

app = FastAPI()


@app.get("/async_sleep")
async def root():
    time.sleep(1)
    return {"message": "Hello World"}


@app.get("/async_sleep_await")
async def root():
    await asyncio.sleep(1)
    return {"message": "Hello World"}


@app.get("/sync_sleep")
def root():
    time.sleep(1)
    return {"message": "Hello World"}
