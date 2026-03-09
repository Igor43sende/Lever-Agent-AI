from fastapi import APIRouter
from app.services.message_processor import process_message
from app.models.message_model import MessageRequest

router = APIRouter()


@router.post("/webhook")
async def receive_message(data: MessageRequest):

    response = process_message(data.dict())

    return {
        "status": "received",
        "response": response
    }