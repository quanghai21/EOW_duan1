from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="Echoes of War API", version="1.0.0")

# Cấu hình CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schemas ---
class Character(BaseModel):
    id: str
    name: str
    avatar_url: str
    voice_id: str

class AvatarChatRequest(BaseModel):
    character_id: str
    message: str

class AvatarChatResponse(BaseModel):
    character_id: str
    reply_text: str
    audio_url: str

class TimelineEvent(BaseModel):
    year: str
    title: str
    description: str

class GalleryItem(BaseModel):
    id: int
    title: str
    image_url: str

class SuggestionResponse(BaseModel):
    character_id: str
    suggested_questions: List[str]
    related_documents: List[dict]


# --- Database giả lập trong bộ nhớ ---
characters_db = [
    {
        "id": "quang-trung",
        "name": "Vua Quang Trung (Nguyễn Huệ)",
        "avatar_url": "/assets/avatars/quangtrung.jpg",
        "voice_id": "vi-VN-Standard-B"
    },
    {
        "id": "tran-hung-dao",
        "name": "Hưng Đạo Đại Vương Trần Quốc Tuấn",
        "avatar_url": "/assets/avatars/tranhungdao.jpg",
        "voice_id": "vi-VN-Standard-D"
    }
]


# --- Route trang chủ ---
@app.get("/")
def read_root():
    return {"message": "Echoes of War Backend is running successfully!"}


# --- 1. CHARACTER APIs (Có đầy đủ GET và POST) ---
@app.get("/api/characters", response_model=List[Character], tags=["Character"])
async def get_characters():
    return characters_db

@app.post("/api/characters", response_model=Character, tags=["Character"])
async def add_character(character: Character):
    for c in characters_db:
        if c["id"] == character.id:
            raise HTTPException(status_code=400, detail="Character ID already exists")
    characters_db.append(character.dict())
    return character


# --- 2. CHAT API ---
@app.post("/api/chat", response_model=AvatarChatResponse, tags=["Chat"])
async def avatar_chat(payload: AvatarChatRequest):
    reply = f"Ta là {payload.character_id}. Ta đã nhận được câu hỏi: '{payload.message}'."
    audio_src = f"/static/audio/{payload.character_id}_speech.mp3"
    
    return AvatarChatResponse(
        character_id=payload.character_id,
        reply_text=reply,
        audio_url=audio_src
    )


# --- 3. SPEECH APIs ---
@app.post("/api/speech/stt", tags=["Speech"])
async def speech_to_text(file: UploadFile = File(...)):
    contents = await file.read()
    return {"text": "Nội dung giọng nói đã được chuyển thành văn bản thành công."}


# --- 4. SUGGESTIONS API ---
@app.get("/api/avatar/suggestions/{character_id}", response_model=SuggestionResponse, tags=["Avatar"])
async def get_suggestions(character_id: str):
    return SuggestionResponse(
        character_id=character_id,
        suggested_questions=[
            "Ngài đã chuẩn bị chiến lược gì cho trận chiến?",
            "Hoàn cảnh lịch sử lúc bấy giờ ra sao?"
        ],
        related_documents=[
            {"title": "Tài liệu lưu trữ lịch sử", "url": "/docs/tai-lieu.pdf"}
        ]
    )


# --- 5. TIMELINE API ---
@app.get("/api/timeline/{character_id}", response_model=List[TimelineEvent], tags=["Timeline"])
async def get_timeline(character_id: str):
    return [
        {"year": "1288", "title": "Trận Bạch Đằng", "description": "Đại thắng quân Nguyên Mông lần thứ 3."},
        {"year": "1285", "title": "Hội nghị Bình Than", "description": "Hội nghị bàn kế sách đánh giặc giữ nước."}
    ]


# --- 6. GALLERY APIs ---
@app.get("/api/gallery/{character_id}", response_model=List[GalleryItem], tags=["Gallery"])
async def get_gallery(character_id: str):
    return [
        {"id": 1, "title": "Bức họa tư liệu gốc", "image_url": "https://via.placeholder.com/300"},
        {"id": 2, "title": "Bản đồ chiến dịch", "image_url": "https://via.placeholder.com/300"}
    ]

@app.post("/api/gallery/upload", tags=["Gallery"])
async def upload_gallery_image(file: UploadFile = File(...)):
    os.makedirs("static/uploads", exist_ok=True)
    file_path = f"static/uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "Upload ảnh thành công", "image_url": f"/{file_path}"}