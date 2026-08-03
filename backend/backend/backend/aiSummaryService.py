import os
import google.generativeai as genai

# Cấu hình API Key (Lấy từ biến môi trường hệ thống)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)

def summarize_learning_history(chat_history_text: str) -> str:
    """
    Sử dụng Gemini AI để tóm tắt các điểm chính từ lịch sử học tập/hội thoại của người dùng.
    """
    try:
        # Sử dụng model chuẩn phù hợp
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Bạn là một trợ lý giáo dục lịch sử thông minh trong dự án 'Echoes of War'. 
        Hãy đọc đoạn lịch sử trò chuyện/học tập sau đây và viết một bản tóm tắt ngắn gọn 
        gồm 3 ý chính: Các sự kiện đã thảo luận, Nhân vật lịch sử liên quan, và Bài học rút ra.

        Nội dung:
        {chat_history_text}
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Lỗi khi kết nối với AI Summary: {str(e)}"

if __name__ == "__main__":
    # Test thử dịch vụ tóm tắt
    sample_history = "Người dùng đã trò chuyện với nhân vật Võ Nguyên Giáp về chiến dịch Điện Biên Phủ, tìm hiểu về khó khăn khi vận chuyển pháo vào mặt trận."
    print("--- Đang test AI Summary ---")
    print(summarize_learning_history(sample_history))