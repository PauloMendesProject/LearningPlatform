# 🤖 AI-Powered Personalized Learning Platform

An intelligent learning assistant that provides instant feedback on **quizzes** and **essays** using OpenAI's GPT-4o — all built with a clean frontend and a lightweight Flask backend.

---

## 🧠 Features

### 📝 Quiz Helper
- Input a quiz question and your answer.
- Choose whether to **reveal the correct answer**.
- Get clear feedback and tips on your understanding.

### 📄 Essay Feedback
- Paste any essay, paragraph, or writing sample.
- Receive AI-generated suggestions on structure, clarity, and grammar.

---

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **AI Integration:** GPT-4o via GitHub's Copilot API
- **Environment Management:** `python-dotenv`

---

## 🛠️ Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/PauloMendesProject/LearningPlatform.git
   cd LearningPlatform

Install Python Dependencies
```bash
pip install -r requirements.txt
```

Create a .env file in the root directory and add your GitHub Copilot API token:
```
GITHUB_TOKEN=your_token_here
```

Run the Flask backned
```
python app.py
```

Open the app
```
Open frontend/index.html directly in your browser.
```

📁 Project Structure
├── app.py                 # Flask backend logic and endpoints

├── requirements.txt       # Python dependencies

├── .env                   # API key (not committed to repo)

└── frontend/
    ├── index.html         # Web interface
    ├── style.css          # Styling and layout
    └── script.js          # JS for frontend-backend communication

📌 Example Use Case
Quiz Example:

Question: What is a closure in JavaScript?
Your Answer: A closure is a function with access to variables in its outer scope.

The assistant will respond with an explanation, correct your understanding if needed, and optionally show the right answer.

Essay Example:
Paste your essay, and you'll get clear AI feedback on clarity, structure, and tone.




