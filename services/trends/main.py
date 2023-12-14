import os

from fastapi.concurrency import asynccontextmanager
from src.apis import apis
from src.prisma import prisma
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(application: FastAPI):
    print("Connect")
    await prisma.connect()
    yield
    await prisma.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(apis, prefix="/v1")

@app.get("/")
def read_root():
    return {"version": "1.0.0"}
