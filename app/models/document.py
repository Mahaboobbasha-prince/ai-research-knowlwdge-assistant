from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime

from app.database.database import Base 
from app.database.database import SessionLocal


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    title = Column(String, nullable=True)

    author = Column(String, nullable=True)

    content = Column(Text, nullable=True)

    upload_time = Column(DateTime, default=datetime.utcnow)