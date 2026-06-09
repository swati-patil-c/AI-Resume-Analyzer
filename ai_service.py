from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print("API Key Loaded:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    
)
def ask_resume_ai(resume_text, user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Hello"}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OPENAI ERROR:", e)
        return f"AI Error: {e}"