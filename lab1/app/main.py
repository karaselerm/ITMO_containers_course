from fastapi import FastAPI
from routers import router as hello_router

app = FastAPI()

app.include_router(hello_router)
