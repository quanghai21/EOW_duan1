from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.chat import router as chat_router
from app.api.character import router as character_router
from app.api.history import router as history_router
from app.api.conversation import router as conversation_router


app = FastAPI(
    title="Echoes of War API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    character_router,
    prefix="/api",
    tags=["Character"]
)


app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)


app.include_router(
    history_router,
    prefix="/api",
    tags=["History"]
)


app.include_router(
    conversation_router,
    prefix="/api",
    tags=["Conversation"]
)


app.mount(
    "/images",
    StaticFiles(directory="images"),
    name="images"
)


@app.get("/")
def root():

    return {
        "project": "Echoes of War",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }