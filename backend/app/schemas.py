from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MessageCreate(BaseModel):
    sender: str
    content: str

class Message(MessageCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class SessionCreate(BaseModel):
    user_id: int

class Session(BaseModel):
    id: int
    started_at: datetime
    messages: List[Message] = []

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str
    sessions: List[Session] = []

    class Config:
        orm_mode = True


class ChatRequest(BaseModel):
    user_id: int
    message: str
    session_id: Optional[int] = None

class ChatResponse(BaseModel):
    session_id: int
    response: str