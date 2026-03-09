from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    role = Column(String)  # user ou assistant
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)