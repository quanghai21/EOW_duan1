from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Echoes of War - Learning & Engagement API", version="1.0")

class BookmarkSchema(BaseModel):
    user_id: str
    item_id: str
    title: str
    category: str

class ProgressUpdateSchema(BaseModel):
    user_id: str
    study_minutes_added: int
    quiz_completed: bool

fake_bookmarks_db = []
fake_progress_db = {
    "user_001": {
        "total_study_minutes": 45,
        "completed_quizzes_count": 2,
        "current_level": "Novice Historian"
    }
}

@app.get("/")
def home():
    return {"message": "Welcome to Echoes of War Learning & Engagement API! Visit /docs for Swagger UI."}

@app.post("/api/bookmarks/add")
def add_bookmark(bookmark: BookmarkSchema):
    fake_bookmarks_db.append(bookmark.dict())
    return {"status": "success", "message": "Đã lưu bookmark thành công!", "data": bookmark}

@app.get("/api/bookmarks/{user_id}")
def get_user_bookmarks(user_id: str):
    user_bookmarks = [b for b in fake_bookmarks_db if b["user_id"] == user_id]
    return {"status": "success", "user_id": user_id, "bookmarks": user_bookmarks}

@app.get("/api/progress/{user_id}")
def get_user_progress(user_id: str):
    progress = fake_progress_db.get(user_id, {
        "total_study_minutes": 0,
        "completed_quizzes_count": 0,
        "current_level": "Novice Historian"
    })
    return {"status": "success", "user_id": user_id, "progress": progress}

@app.post("/api/progress/update")
def update_progress(data: ProgressUpdateSchema):
    if data.user_id not in fake_progress_db:
        fake_progress_db[data.user_id] = {
            "total_study_minutes": 0,
            "completed_quizzes_count": 0,
            "current_level": "Novice Historian"
        }
    
    user_prog = fake_progress_db[data.user_id]
    user_prog["total_study_minutes"] += data.study_minutes_added
    if data.quiz_completed:
        user_prog["completed_quizzes_count"] += 1
        
    if user_prog["completed_quizzes_count"] >= 5:
        user_prog["current_level"] = "Expert Historian"
    elif user_prog["completed_quizzes_count"] >= 3:
        user_prog["current_level"] = "Intermediate Historian"

    return {"status": "success", "message": "Đã cập nhật tiến độ!", "progress": user_prog}