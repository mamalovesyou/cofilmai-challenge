import io
import yaml
import functools

from fastapi.concurrency import asynccontextmanager
from src.apis import apis
from src.prisma import prisma
from fastapi import FastAPI
from fastapi.responses import Response


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

# ./openapi/api.cofilm.yaml creator endpoint
@app.get('/openapi.yaml', include_in_schema=False)
@functools.lru_cache()
def read_openapi_yaml() -> Response:
    openapi_json = app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s)
    return Response(yaml_s.getvalue(), media_type='text/yaml')
