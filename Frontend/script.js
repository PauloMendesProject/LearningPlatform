// frontend/script.js

const BACKEND_URL = "http://127.0.0.1:5000"; // adjust if needed

async function submitQuiz() {
  const question = document.getElementById("quiz-question").value;
  const answer = document.getElementById("quiz-answer").value;
  const reveal = document.getElementById("reveal-answer")?.checked || false;

  const res = await fetch(`${BACKEND_URL}/submit_quiz`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      question,
      answer,
      reveal
    }),
  });

  const data = await res.json();
  document.getElementById("quiz-result").innerText = data.response || data.error;
}

async function submitEssay() {
  const essay = document.getElementById("essay-text").value;

  const res = await fetch(`${BACKEND_URL}/submit_essay`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ essay: essay }),
  });

  const data = await res.json();
  document.getElementById("essay-result").innerText = data.analysis || data.error;
}
