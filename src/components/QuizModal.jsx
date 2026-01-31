export default function QuizModal({ quiz, onClose }) {
  return (
    <div className="modal">
      <div className="modal-content">
        <button className="close" onClick={onClose}>✖</button>
        <h2>{quiz.title}</h2>
        <p>{quiz.summary}</p>

        {quiz.quiz.map((q, i) => (
          <div key={i}>
            <b>{q.question}</b>
            <p>Answer: {q.answer}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
