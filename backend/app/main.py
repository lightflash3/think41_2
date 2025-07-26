from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base
from typing import List, Optional, Dict

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/sessions/", response_model=schemas.Session)
def create_chat_session(session: schemas.SessionCreate, db: Session = Depends(get_db)):
    return crud.create_session(db, session)

@app.post("/sessions/{session_id}/messages/", response_model=schemas.Message)
def post_message(session_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, session_id, message)

@app.get("/users/{user_id}/sessions/", response_model=List[schemas.Session])
def get_user_sessions(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_sessions(db, user_id)

@app.get("/sessions/{session_id}/messages/", response_model=List[schemas.Message])
def get_session_messages(session_id: int, db: Session = Depends(get_db)):
    return crud.get_session_messages(db, session_id)
