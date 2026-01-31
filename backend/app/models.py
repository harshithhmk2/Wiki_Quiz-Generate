from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from .database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text)
    key_entities = Column(JSONB)
    sections = Column(JSONB)
    quiz = Column(JSONB)
    related_topics = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
