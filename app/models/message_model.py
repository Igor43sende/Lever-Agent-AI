from pydantic import BaseModel


class MessageRequest(BaseModel):
    user: str
    message: str