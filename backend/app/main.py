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








from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import router từ mô-đun knowledge_cms của bạn
from app.knowledge_cms.cms_api import router as knowledge_router

app = FastAPI(
    title="Echoes of War - Knowledge Management System",
    description="API hệ thống quản lý tri thức và nhập vai nhân vật lịch sử",
    version="1.0.0"
)

# Cấu hình CORS để React (chạy ở cổng 5173/3000) có thể gửi yêu cầu lên Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Có thể đổi thành ["http://localhost:5173"] nếu muốn bảo mật hơn
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký Router Quản lý Tri thức (Knowledge CMS)
app.include_router(knowledge_router)

@app.get("/")
async def root():
    return {"message": "Echoes of War API Gateway đang hoạt động bình thường!"}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.knowledge_cms.cms_api import router as knowledge_router

app = FastAPI(title="Echoes of War")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký router
app.include_router(knowledge_router)