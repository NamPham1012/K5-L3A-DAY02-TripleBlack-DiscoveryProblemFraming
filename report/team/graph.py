import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langgraph.prebuilt import create_react_agent

# 1. Cấu hình API Key của NVIDIA (Bạn thay đoạn trong nháy kép bằng API Key thực tế của bạn)
os.environ["NVIDIA_API_KEY"] = "nvapi-dien_khoa_api_cua_ban_vao_day"

# 2. Khởi tạo mô hình Nemotron 3.5 Bolt BF16 theo yêu cầu của thầy
llm = ChatNVIDIA(
    model="nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16",
    temperature=0.2,
)

# 3. Định nghĩa System Prompt cho TravelBuddy (tuân thủ quy tắc Lab 4)
system_prompt = """
Bạn là TravelBuddy - một Agent du lịch thông minh bằng tiếng Việt.
Quy tắc hoạt động:
1. Thứ tự gọi tool bắt buộc qua chuỗi: search_flights -> calculate_budget -> search_hotels.
2. Luôn hỏi lại người dùng nếu thông tin chuyến đi (điểm đi, điểm đến, ngày tháng) chưa đầy đủ.
3. Từ chối trả lời các yêu cầu nguy hiểm hoặc vi phạm pháp luật.
4. Chỉ sử dụng dữ liệu số liệu thực tế được trả về từ các tool, không tự bịa đặt.
"""

# 4. Khởi tạo Agent hoàn chỉnh kết hợp 3 tools và system prompt
# (Lưu ý: các hàm search_flights, calculate_budget, search_hotels đã được định nghĩa ở các file tool của bạn)
agent = create_react_agent(
    model=llm,
    tools=[search_flights, calculate_budget, search_hotels],
    prompt=system_prompt,
)