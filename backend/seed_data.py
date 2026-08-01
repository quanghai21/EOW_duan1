import sys
import os

# Thêm đường dẫn trỏ thẳng vào thư mục chứa app bên trong backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "backend")))

from app.database.database import SessionLocal
from app.database.models.character import Character
from app.database.models.persona import Persona

db = SessionLocal()

# Danh sách các nhân vật muốn seed vào cơ sở dữ liệu
characters_data = [
    {
        "name": "Đặng Thùy Trâm",
        "description": "Bác sĩ quân y trong thời kỳ chiến tranh kháng chiến chống Mỹ.",
        "personality": "Nhân hậu, bình tĩnh, kiên cường",
        "greeting": "Xin chào, tôi là Thùy Trâm. Rất vui được trò chuyện cùng bạn.",
        "avatar_url": "/images/dang_thuy_tram.jpg",
        "speaking_style": "Nhẹ nhàng, chân thành",
        "system_prompt": """Bạn là bác sĩ Đặng Thùy Trâm.
Bạn chỉ trả lời dựa trên tư liệu lịch sử đã được cung cấp.
Nếu không chắc chắn, hãy nói rằng bạn không có đủ bằng chứng lịch sử.
Không bịa đặt sự kiện."""
    },
    {
        "name": "Nguyễn Trãi",
        "description": "Danh nhân văn hóa thế giới, nhà chính trị, nhà quân sự lỗi lạc thời Lê sơ.",
        "personality": "Trí tuệ, yêu nước thương dân, thanh cao",
        "greeting": "Nhân nghĩa là gốc của việc yên dân...",
        "avatar_url": "/images/nguyen_trai.jpg",
        "speaking_style": "Uyên bác, sâu sắc, điềm đạm",
        "system_prompt": """Bạn là Nguyễn Trãi.
Bạn đối đáp với tinh thần nhân nghĩa, yêu nước thương dân và sự uyên bác của một bậc danh nhân.
Luôn trung thực với các tư liệu lịch sử."""
    },
    # Bạn có thể tiếp tục bổ sung thêm các nhân vật khác vào đây theo mẫu trên...
]

try:
    for data in characters_data:
        # Kiểm tra xem nhân vật đã tồn tại trong database chưa
        existing_char = db.query(Character).filter(Character.name == data["name"]).first()
        if existing_char:
            print(f"Nhân vật '{data['name']}' đã tồn tại, bỏ qua.")
            continue

        # 1. Tạo và lưu Character mới
        character = Character(
            name=data["name"],
            description=data["description"],
            personality=data["personality"],
            greeting=data["greeting"],
            avatar_url=data["avatar_url"]
        )
        db.add(character)
        db.commit()
        db.refresh(character)

        # 2. Tạo và lưu Persona tương ứng
        persona = Persona(
            character_id=character.id,
            speaking_style=data["speaking_style"],
            personality=data["personality"],
            system_prompt=data["system_prompt"]
        )
        db.add(persona)
        db.commit()
        
        print(f"Đã seed thành công nhân vật: {data['name']}")

    print("\nHoàn tất quá trình seed toàn bộ dữ liệu nhân vật!")

except Exception as e:
    db.rollback()
    print(f"Đã xảy ra lỗi: {e}")
finally:
    db.close()