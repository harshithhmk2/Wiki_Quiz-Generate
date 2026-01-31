from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class QuizBase(BaseModel):
    url: str
    title: str
    summary: str
    key_entities: Dict[str, Any]
    sections: List[str]
    quiz: List[Dict[str, Any]]
    related_topics: List[str]

class QuizResponse(QuizBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

