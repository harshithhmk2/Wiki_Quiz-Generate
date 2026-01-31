from fastapi import FastAPI
from .database import engine, Base
from .routes.quiz import router as quiz_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wiki Quiz Generator",
    description="Generate quizzes from Wikipedia using Groq LLM",
    version="1.0.0"
)

app.include_router(quiz_router)

@app.get("/")
def root():
    return {"status": "Wiki Quiz API is running"}
