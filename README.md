# 📘 Wiki Quiz Generator

A full-stack application that generates quizzes automatically from Wikipedia articles using a Large Language Model (Groq).  
The system scrapes Wikipedia content, generates structured quizzes, stores them in a database, and displays them via a clean React UI.

---

## 🚀 Features

- Accepts any valid Wikipedia article URL
- Scrapes article content using HTML scraping (BeautifulSoup)
- Generates:
  - Article summary
  - Key entities (people, organizations, locations)
  - 5–10 multiple-choice questions
  - Difficulty level & explanation for each question
  - Related topics for further reading
- Stores all quizzes for future access
- History view with detailed quiz modal
- Optional “Take Quiz” mode (answers revealed on demand)

---

## 🧱 Tech Stack

### Backend
- FastAPI
- Groq LLM (LLaMA‑3.1‑8B‑Instant)
- BeautifulSoup (HTML scraping)
- SQLAlchemy ORM
- Neon PostgreSQL (cloud database)

### Frontend
- React (Create React App)
- Axios
- Plain CSS (minimal UI)

---

## 📂 Project Structure

```
wiki-quiz/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── routes/
│   │   │   └── quiz.py
│   │   └── services/
│   │       ├── scraper.py
│   │       └── llm.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── GenerateQuiz.jsx
│   │   │   ├── History.jsx
│   │   │   ├── QuizCard.jsx
│   │   │   └── QuizModal.jsx
│   │   ├── App.jsx
│   │   ├── api.js
│   │   ├── index.js
│   │   └── styles.css
│   └── package.json
│
├── sample_data/
│   ├── urls.txt
│   └── alan_turing.json
│
├── screenshots/
│   ├── tab1_generate_quiz.png
│   ├── tab2_history.png
│   └── quiz_details_modal.png
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

Create `.env` file inside `backend/`:

```env
DATABASE_URL=postgresql://<user>:<password>@<neon-host>/<db>?sslmode=require
GROQ_API_KEY=<your_groq_api_key>
```

Run backend:

```bash
uvicorn app.main:app --reload
```

API:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend:
```
http://localhost:3000
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/` | Health check |
| POST | `/quiz/generate` | Generate quiz |
| GET | `/quiz/history` | List all quizzes |
| GET | `/quiz/{quiz_id}` | Quiz details |

---

## 🧪 Sample Data

Sample Wikipedia URLs:
- https://en.wikipedia.org/wiki/Alan_Turing
- https://en.wikipedia.org/wiki/Narendra_Modi

Stored in:
```
sample_data/
```

---

## 📸 Screenshots Checklist

- Generate Quiz page (Tab 1)
- History view (Tab 2)
- Quiz details modal

Stored in:
```
screenshots/
```

---

## 🧠 Project Flow

1. User submits Wikipedia URL
2. Backend scrapes article content
3. Content sent to Groq LLM for quiz generation
4. Quiz stored in Neon PostgreSQL
5. Frontend displays quiz and history

---

## 🏁 Submission Checklist

- Backend complete
- Frontend UI complete
- Groq LLM integrated
- Neon PostgreSQL connected
- Sample data added
- Screenshots captured
- README finalized

---

## 💬 Short Explanation

“This project scrapes Wikipedia articles, generates structured quizzes using Groq’s LLaMA model, stores results in a cloud PostgreSQL database, and exposes REST APIs consumed by a React frontend.”

---

✅ **Project is submission‑ready**
