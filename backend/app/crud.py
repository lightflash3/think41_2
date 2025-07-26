from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_session(db: Session, session: schemas.SessionCreate):
    db_session = models.Session(user_id=session.user_id)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def create_message(db: Session, session_id: int, message: schemas.MessageCreate):
    db_message = models.Message(session_id=session_id, sender=message.sender, content=message.content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_user_sessions(db: Session, user_id: int):
    return db.query(models.Session).filter(models.Session.user_id == user_id).all()

def get_session_messages(db: Session, session_id: int):
    return db.query(models.Message).filter(models.Message.session_id == session_id).order_by(models.Message.timestamp).all()
