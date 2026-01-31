import { useState } from "react";
import api from "../api";
import QuizCard from "./QuizCard";

export default function GenerateQuiz() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateQuiz = async () => {
    setLoading(true);
    try {
      const res = await api.post("/quiz/generate", null, {
        params: { url },
      });
      setQuiz(res.data);
    } catch (err) {
      alert("Failed to generate quiz");
    }
    setLoading(false);
  };

  return (
    <>
      <div className="input-box">
        <input
          placeholder="Enter Wikipedia URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={generateQuiz} disabled={loading}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>
      </div>

      {quiz && <QuizCard quiz={quiz} />}
    </>
  );
}
