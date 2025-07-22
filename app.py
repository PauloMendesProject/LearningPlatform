from dotenv import load_dotenv
load_dotenv()

from flask_cors import CORS

import os
import openai

# app.py

from flask import Flask, request, jsonify

# Load GitHub token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Configure OpenAI client for GitHub AI Marketplace
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=GITHUB_TOKEN
)

# Create a Flask application instance

app = Flask(__name__)
CORS(app)

# Route to handle quiz submissions sent via POST request
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data = request.get_json()
    print("Received data:", data)
    question = data.get("question", "")
    answer = data.get("answer", "")
    reveal_answer = data.get("reveal", False)  # optional toggle

    if not question or not answer:
        return jsonify({"error": "Question and answer are required"}), 400

    try:
        messages = [
            {"role": "system", "content": "You are a helpful tutor who guides users to the right answer without giving it away unless explicitly asked."},
            {"role": "user", "content": f"Question: {question}\nStudent's answer: {answer}"}
        ]

        if reveal_answer:
            messages.append({"role": "user", "content": "Can you now tell me the correct answer?"})

        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )

        ai_reply = response.choices[0].message.content
        return jsonify({"response": ai_reply})

    except Exception as e:
        return jsonify({"error": f"Quiz AI error: {str(e)}"}), 500

# Essay analysis endpoint using GPT-4o from GitHub AI
@app.route('/submit_essay', methods=['POST'])
def submit_essay():
    data = request.get_json()
    essay_text = data.get('essay', '')

    if not essay_text:
        return jsonify({"error": "Essay text is required"}), 400

    prompt = f"Analyze the following essay for grammar, structure, and provide suggestions for improvement:\n\n{essay_text}"

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert essay reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        analysis_text = response.choices[0].message.content
        return jsonify({"analysis": analysis_text})

    except Exception as e:
        return jsonify({"error": f"GPT-4o Error: {str(e)}"}), 500


# Run flask app only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)