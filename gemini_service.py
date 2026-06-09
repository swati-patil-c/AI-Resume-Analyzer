import google.generativeai as genai

genai.configure(api_key="YOUR_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")


def ask_gemini_ai(resume, message):
    response = model.generate_content(f"""
You are a resume AI assistant.

Resume:
{resume}

Question:
{message}
""")

    return response.text