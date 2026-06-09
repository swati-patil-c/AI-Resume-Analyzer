from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
<<<<<<< HEAD
from ai_service import ask_resume_ai
import json
=======
from dual_ai import ask_resume_ai
>>>>>>> f08a825 (clean project)
import os
import re
import uuid

<<<<<<< HEAD

app = Flask(__name__)

UPLOAD_FOLDER  = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER , exist_ok=True)
=======
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

>>>>>>> f08a825 (clean project)

@app.route("/")
def home():
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/analyze", methods=["POST"])
def analyze():

    
    if "resume" not in request.files:
        return "Please upload a resume."
    
=======

@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "Please upload a resume."

>>>>>>> f08a825 (clean project)
    resume = request.files["resume"]

    if resume.filename == "":
        return "No file selected."
<<<<<<< HEAD
    
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
=======

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
        return "No readable text found."

    if not job_description.strip():
        return "Please enter job description."
>>>>>>> f08a825 (clean project)

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
<<<<<<< HEAD

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = round(similarity[0][0] * 100,2)
    
=======
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)

>>>>>>> f08a825 (clean project)
    if score >= 80:
        status = "Excellent Match"
    elif score >= 60:
        status = "Good Match"
    elif score >= 40:
        status = "Average Match"
    else:
        status = "Needs Improvement"

<<<<<<< HEAD
    resume_words = set(
        re.findall(r"\b[a-zA-Z]+\b", resume_text.lower())
    )

    job_words = set(
        re.findall(r"\b[a-zA-Z]+\b", job_description.lower())
    )
=======
    resume_words = set(re.findall(r"\b[a-zA-Z]+\b", resume_text.lower()))
    job_words = set(re.findall(r"\b[a-zA-Z]+\b", job_description.lower()))
>>>>>>> f08a825 (clean project)

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
<<<<<<< HEAD
        suggestions.append("Include projects matching the job description.")
        suggestions.append("Mention tools and technologies used.")
    else:
        suggestions.append("Resume match the job description well.")
=======
        suggestions.append("Include projects matching job description.")
    else:
        suggestions.append("Your resume matches well.")

>>>>>>> f08a825 (clean project)
    return render_template(
        "result.html",
        filename=filename,
        score=score,
<<<<<<< HEAD
        resume_text=resume_text,
        status=status,
        job_description=job_description,
        suggestions=suggestions,
        missing_keywords=missing_keywords

=======
        status=status,
        resume_text=resume_text,
        job_description=job_description,
        missing_keywords=missing_keywords,
        suggestions=suggestions
>>>>>>> f08a825 (clean project)
    )


@app.route("/chat", methods=["POST"])
def chat():
<<<<<<< HEAD
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
=======
    data = request.get_json()

    message = data.get("message", "")
    resume = data.get("resume", "")

    reply = ask_resume_ai(resume, message)

    return {"reply": reply}


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> f08a825 (clean project)
