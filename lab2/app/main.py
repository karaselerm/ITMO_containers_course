from api.routers import hello_router, users_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(hello_router)
app.include_router(users_router)
