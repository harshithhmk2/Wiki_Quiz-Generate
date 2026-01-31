import { useEffect, useState } from "react";
import api from "../api";
import QuizModal from "./QuizModal";

export default function History() {
  const [quizzes, setQuizzes] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    api.get("/quiz/history").then((res) => setQuizzes(res.data));
  }, []);

  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>URL</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {quizzes.map((q) => (
            <tr key={q.id}>
              <td>{q.title}</td>
              <td>{q.url}</td>
              <td>
                <button onClick={() => setSelected(q)}>Details</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selected && (
        <QuizModal quiz={selected} onClose={() => setSelected(null)} />
      )}
    </>
  );
}
