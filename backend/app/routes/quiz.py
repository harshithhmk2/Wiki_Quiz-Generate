from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from urllib.parse import unquote

from ..database import get_db
from ..services.scraper import scrape_wikipedia
from ..services.llm import generate_quiz
from ..crud import (
    get_quiz_by_url,
    create_quiz,
    get_all_quizzes,
    get_quiz_by_id
)
from ..schemas import QuizResponse

router = APIRouter(prefix="/quiz", tags=["Quiz"])


# -------------------------------------------------
# POST /quiz/generate
# -------------------------------------------------
@router.post("/generate", response_model=QuizResponse)
def generate_quiz_api(url: str, db: Session = Depends(get_db)):
    # 🔒 Sanitize URL
    url = unquote(url).strip()

    # 🔒 Validate Wikipedia URL
    if not url.startswith("https://en.wikipedia.org/wiki/"):
        raise HTTPException(
            status_code=400,
            detail="Only valid Wikipedia article URLs are allowed"
        )

    # 🔁 Avoid duplicate processing
    existing = get_quiz_by_url(db, url)
    if existing:
        return existing

    # 🌐 Scrape Wikipedia
    try:
        scraped = scrape_wikipedia(url)
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=f"Failed to scrape Wikipedia page: {str(e)}"
        )

    # 🤖 Generate quiz using Groq
    try:
        ai_data = generate_quiz(scraped["content"])
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM failed to generate quiz: {str(e)}"
        )

    # 🧹 Normalize summary
    summary = ai_data.get("summary", "")
    if isinstance(summary, dict):
        summary = " ".join(summary.values())
    elif isinstance(summary, list):
        summary = " ".join(summary)
    elif not isinstance(summary, str):
        summary = str(summary)

    quiz_data = {
        "url": url,
        "title": scraped["title"],
        "summary": summary,
        "key_entities": ai_data["key_entities"],
        "sections": scraped["sections"],
        "quiz": ai_data["quiz"],
        "related_topics": ai_data["related_topics"]
    }

    return create_quiz(db, quiz_data)


# -------------------------------------------------
# GET /quiz/history   ✅ (THIS WAS MISSING)
# -------------------------------------------------
@router.get("/history", response_model=list[QuizResponse])
def quiz_history(db: Session = Depends(get_db)):
    """
    Returns all previously generated quizzes
    """
    return get_all_quizzes(db)


# -------------------------------------------------
# GET /quiz/{quiz_id} ✅ (THIS WAS MISSING)
# -------------------------------------------------
@router.get("/{quiz_id}", response_model=QuizResponse)
def quiz_details(quiz_id: int, db: Session = Depends(get_db)):
    """
    Returns a single quiz by ID
    """
    quiz = get_quiz_by_id(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz
