import { useState } from "react";
import GenerateQuiz from "./components/GenerateQuiz";
import History from "./components/History";
import "./styles.css";

export default function App() {
  const [tab, setTab] = useState("generate");

  return (
    <div className="container">
      <h1>📘 Wiki Quiz Generator</h1>

      <div className="tabs">
        <button
          className={tab === "generate" ? "active" : ""}
          onClick={() => setTab("generate")}
        >
          Generate Quiz
        </button>
        <button
          className={tab === "history" ? "active" : ""}
          onClick={() => setTab("history")}
        >
          Past Quizzes
        </button>
      </div>

      {tab === "generate" ? <GenerateQuiz /> : <History />}
    </div>
  );
}
