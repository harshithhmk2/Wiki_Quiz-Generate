import { useState } from "react";

export default function QuizCard({ quiz }) {
  const [showAnswers, setShowAnswers] = useState(false);

  return (
    <div className="card">
      <h2>{quiz.title}</h2>
      <p>{quiz.summary}</p>

      <h3>Quiz</h3>
      {quiz.quiz.map((q, idx) => (
        <div key={idx} className="question">
          <b>{idx + 1}. {q.question}</b>
          <ul>
            {q.options.map((opt, i) => (
              <li key={i}>{opt}</li>
            ))}
          </ul>

          {showAnswers && (
            <p className="answer">
              ✅ <b>{q.answer}</b> — {q.explanation}
            </p>
          )}
        </div>
      ))}

      <button onClick={() => setShowAnswers(!showAnswers)}>
        {showAnswers ? "Hide Answers" : "Take Quiz"}
      </button>

      <h4>Related Topics</h4>
      <ul>
        {quiz.related_topics.map((t, i) => (
          <li key={i}>{t}</li>
        ))}
      </ul>
    </div>
  );
}
