from fastapi import FastAPI, HTTPException
import google.generativeai as genai
from pydantic import BaseModel, Field #Xac thuc du lieu dau vao

from chatservice import (
    check_configure_genai,
    send_user_message_to_gemini,
    get_chat_history
)



import logging
#Cau hinh log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#Cau hinh API key
check_configure_genai(api_key="AIzaSyCsTV4RbsJUn78lvd_THDmttYRnZN2aL6k")
model = genai.GenerativeModel("gemini-1.5-flash")


app = FastAPI(
    title="CHAT BOT WITH API KEY GEMINI",
    description="API ĐỂ TƯƠNG TÁC VỚI GEMINI CHAT BOT",
    version="1.0.0"
)

#Models
class ChatRequest(BaseModel):
    user_id: str = Field(..., description="ID của người dùng")
    message: str = Field(..., description="Nội dung của tin nhắn")


class HistoryRequest(BaseModel):
    user_id: str
#Routes
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        logger.info(f"Nhận tin nhắn từ user_id: {request.user_id}")
        result = send_user_message_to_gemini(request.user_id, request.message, model)
        return result
    except Exception as e:
        logger.error(f"Lỗi khi xủ lý tin nhắn: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat/history")
async def get_history(request: HistoryRequest):
    try:
        logger.info(f"Lấy lịch sử chat cho user_id: {request.user_id}")
        history = get_chat_history(request.user_id, model)
        return [{"user_id": request.user_id, "history_chat": history}]
    except Exception as e:
        logger.error(f"Lỗi khi lấy lịch sử chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

