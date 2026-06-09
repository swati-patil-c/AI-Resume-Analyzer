from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ai_service import ask_resume_ai
import json
import os
import re
import uuid


app = Flask(__name__)

UPLOAD_FOLDER  = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER , exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    
    if "resume" not in request.files:
        return "Please upload a resume."
    
    resume = request.files["resume"]

    if resume.filename == "":
        return "No file selected."
    
    if not resume.filename.lower().endswith(".pdf"):
        return "ONLY PDF FILE IS ALLOWED."
    
    job_description = request.form.get("job_description", "")


    filename = str(uuid.uuid4()) + "_" + resume.filename
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    
    resume.save(filepath)
    reader = PdfReader(filepath)

    resume_text = ""

    for page in reader.pages:
       text = page.extract_text()
       if text:
           resume_text += text
    
    if not resume_text.strip():
        return "No readable text found. Please upload a text-based PDF."
    if not resume_text.strip():
        return "No text could be extracted from the uploaded PDF."

    if not job_description.strip():
        return "Please enter job description."
    #compare resume with job secription

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = round(similarity[0][0] * 100,2)
    
    if score >= 80:
        status = "Excellent Match"
    elif score >= 60:
        status = "Good Match"
    elif score >= 40:
        status = "Average Match"
    else:
        status = "Needs Improvement"

    resume_words = set(
        re.findall(r"\b[a-zA-Z]+\b", resume_text.lower())
    )

    job_words = set(
        re.findall(r"\b[a-zA-Z]+\b", job_description.lower())
    )

    skills = [
        "python", "java", "html", "css", "javascript",
        "php", "mysql", "flask", "django", "react",
        "git", "docker", "aws", "sql", "tensorflow",
        "nlp", "android", "firebase", "mongodb"
    ]

    missing_keywords = [
        skill for skill in skills
        if skill in job_words and skill not in resume_words
    ]

    suggestions = []
    if score < 50:
        suggestions.append("Add more relevant technical skills.")
        suggestions.append("Include projects matching the job description.")
        suggestions.append("Mention tools and technologies used.")
    else:
        suggestions.append("Resume match the job description well.")
    return render_template(
        "result.html",
        filename=filename,
        score=score,
        resume_text=resume_text,
        status=status,
        job_description=job_description,
        suggestions=suggestions,
        missing_keywords=missing_keywords

    )

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        message = data.get("message", "")
        resume = data.get("resume", "")

        reply = ask_resume_ai(resume, message)

        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Server Error: {str(e)}"}
if __name__ == "__main__":
    app.run(debug=True)
