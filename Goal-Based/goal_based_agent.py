import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up Gemini Flash model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Memory to store conversation and user data
chat = model.start_chat(history=[])
application_info = {
    "name": None,
    "email": None,
    "skills": None
}

def extract_info(user_input):
    global application_info
    text = user_input.lower()

    if "name is" in text:
        name = text.split("name is")[1].split(" and")[0].strip().title()
        application_info["name"] = name
    if "email is" in text:
        email = text.split("email is")[1].split(" and")[0].strip()
        application_info["email"] = email
    if "skills are" in text:
        skills = text.split("skills are")[1].strip().replace(".", "")
        application_info["skills"] = skills

    return "✅ Info saved. Let me check if anything's missing..."

def check_goal():
    missing = [k for k, v in application_info.items() if not v]
    if not missing:
        return (
            f"✅ You're ready to apply!\n\n"
            f"**Name**: {application_info['name']}\n"
            f"**Email**: {application_info['email']}\n"
            f"**Skills**: {application_info['skills']}"
        )
    else:
        return f"⏳ Still missing: {', '.join(missing)}. Please provide them."

# Main loop
print("👋 Hi! I'm your job application assistant.")
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    response = extract_info(user_input)
    print("Assistant:", response)

    goal_status = check_goal()
    print("Assistant:", goal_status)
