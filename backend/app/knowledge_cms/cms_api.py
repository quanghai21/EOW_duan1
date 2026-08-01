from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
from app.knowledge_cms.ingestion import DataIngestion
from app.knowledge_cms.metadata_manager import MetadataManager
from app.knowledge_cms.vector_pipeline import VectorPipeline

router = APIRouter(prefix="/api/v1/admin/knowledge", tags=["Knowledge Management"])

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../../../uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def handle_upload(
    title: str = Form(...),
    character_code: str = Form(...),
    time_period: str = Form(""),
    location: str = Form(""),
    tags: str = Form(""),
    file: UploadFile = File(...)
):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = DataIngestion.parse_file(path, file.filename)
    meta = MetadataManager.build_metadata(title, character_code, time_period, location, tags)
    total_chunks = VectorPipeline.index_document(text, meta)

    return {"status": "success", "total_chunks": total_chunks}