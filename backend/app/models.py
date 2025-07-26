from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "chat_users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sessions = relationship("Session", back_populates="user")

class Session(Base):
    __tablename__ = "chat_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("chat_users.id"))
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="sessions")
    messages = relationship("Message", back_populates="session")

class Message(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))
    sender = Column(String)  # 'user' or 'bot'
    content = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    session = relationship("Session", back_populates="messages")
