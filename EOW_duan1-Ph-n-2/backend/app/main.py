from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Import các router
from app.api.chat import router as chat_router
from app.api.character import router as character_router  # <-- Thêm dòng này

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

# Đăng ký router Chat
app.include_router(
    chat_router,
    prefix="/api",
    tags=["Chat"]
)

# Đăng ký router Character (Bổ sung đoạn này)
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