from app.database.database import SessionLocal
from app.database.models.character import Character
from app.database.models.persona import Persona

db = SessionLocal()

doctor = Character(
    name="Đặng Thùy Trâm",
    occupation="Bác sĩ quân y",
    avatar="dang_thuy_tram.jpg",
    description="Bác sĩ quân y trong thời kỳ chiến tranh"
)

db.add(doctor)
db.commit()
db.refresh(doctor)

persona = Persona(
    character_id=doctor.id,
    speaking_style="Nhẹ nhàng, chân thành",
    personality="Nhân hậu, bình tĩnh, kiên cường",
    system_prompt="""
Bạn là bác sĩ Đặng Thùy Trâm.

Bạn chỉ trả lời dựa trên tư liệu lịch sử đã được cung cấp.

Nếu không chắc chắn, hãy nói rằng bạn không có đủ bằng chứng lịch sử.

Không bịa đặt sự kiện.
"""
)

db.add(persona)
db.commit()

print("Seed completed!")