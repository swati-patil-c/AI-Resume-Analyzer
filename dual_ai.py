import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def offline_ai(resume, message):
    msg = message.lower()
    resume = resume.lower()

    if msg.strip() in ["hi", "hello", "hey"]:
        return "Hello! I am your AI Resume Assistant. Ask me about job roles, resume improvement, or skills."

    skills = {
        "python": "Python is strong — good for backend, automation, and AI roles.",
        "java": "Java is useful for enterprise backend and Android development.",
        "sql": "SQL is essential for backend and data roles.",
        "flask": "Flask shows backend API development experience.",
        "django": "Django is strong for full-stack development.",
        "react": "React is ideal for frontend development roles.",
        "ml": "Machine Learning fits AI/ML engineering roles."
    }

    found = [k for k in skills if k in resume]

    if "job" in msg or "suit" in msg or "fit" in msg:
        if "python" in found and "flask" in found:
            return "Best suited role: Backend Developer (Python + Flask). Focus on API projects and deployment."

        if "react" in found:
            return "Best suited role: Frontend Developer. Improve UI projects and build deployed apps."

        if "ml" in found:
            return "Best suited role: AI/ML Engineer. Add prediction and classification projects."

        if "java" in found:
            return "Best suited role: Java Backend or Android Developer."

        return "Best suited role: Entry-level Software Developer. Focus on building 2–3 strong projects."

    if "improve" in msg or "suggestion" in msg:
        tips = []

        if "python" in found:
            tips.append("Build backend projects using Flask or Django.")

        if "sql" in found:
            tips.append("Work on database projects with joins and queries.")

        if "ml" in found:
            tips.append("Create one ML project like prediction or classification model.")

        if len(found) < 3:
            tips.append("Add more technical depth and real-world projects.")

        return "Resume improvement suggestions:\n- " + "\n- ".join(tips)

    for skill in skills:
        if skill in msg:
            return skills[skill]

    if found:
        return "Strong skills in " + ", ".join(found) + ". Next step: build real projects and upload them on GitHub."

    return "Your resume is basic. Start with Python, SQL, and 2 strong projects."


def online_ai(resume, message):
    response = model.generate_content(f"""
You are a resume AI assistant.

Resume:
{resume}

User Question:
{message}
""")
    return response.text


def ask_resume_ai(resume, message):
    try:
        if API_KEY == "YOUR_GEMINI_API_KEY":
            return offline_ai(resume, message)

        return online_ai(resume, message)

    except Exception:
        return offline_ai(resume, message)