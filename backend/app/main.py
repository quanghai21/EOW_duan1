from fastapi import FastAPI

from app.api.chat import router as chat_router

from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Echoes of War API",
    version="1.0.0"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)

from app.api.character import router as character_router

app.include_router(
    character_router,
    prefix="/api",
    tags=["Character"]
)

app.mount(
    "/images",
    StaticFiles(directory="images"),
    name="images",
)