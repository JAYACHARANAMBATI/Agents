import os
import re
import fitz  # PyMuPDF
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")
chat = model.start_chat(history=[])

# Global state
application_info = {"name": None, "email": None, "skills": None}

# PDF Text Extraction
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# Application Info Extraction from PDF
def extract_info_from_cv(text: str):
    extracted_info = {"name": None, "email": None, "skills": None}
    name_match = re.search(r"(?:Full Name:|Name:)\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", text)
    email_match = re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    skills_match = re.search(r"Skills\s*-+\s*(.*?)\n(?:Projects|Certifications|$)", text, re.DOTALL)

    if name_match:
        extracted_info["name"] = name_match.group(1).strip()
    if email_match:
        extracted_info["email"] = email_match.group(0).strip()
    if skills_match:
        skills = skills_match.group(1).replace("\n", ", ").replace("\u2022", "").replace("-", "")
        extracted_info["skills"] = re.sub(r"\s+", " ", skills.strip())

    return extracted_info

# Application Info Extraction from User Input
def extract_application_info(text: str):
    name_match = re.search(r"(?:my name is|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", text, re.IGNORECASE)
    email_match = re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    skills_match = re.search(r"(?:skills are|i know|i can use)\s+(.+)", text, re.IGNORECASE)

    if name_match:
        application_info["name"] = name_match.group(1).title()
    if email_match:
        application_info["email"] = email_match.group(0)
    if skills_match:
        application_info["skills"] = skills_match.group(1).strip()

def check_goal_status():
    if all(application_info.values()):
        return (
            f"✅ You're ready to apply!\n\n"
            f"**Name**: {application_info['name']}\n"
            f"**Email**: {application_info['email']}\n"
            f"**Skills**: {application_info['skills']}"
        )
    else:
        missing = [key for key, value in application_info.items() if not value]
        return f"⏳ Still missing: {', '.join(missing)}"

# Streamlit UI
st.set_page_config(page_title="🎯 Job Application Assistant", layout="centered")
st.title("🧠 Gemini Flash Job Application Assistant")

st.markdown("Tell me your **name**, **email**, and **skills**, or upload your resume!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "goal_complete" not in st.session_state:
    st.session_state.goal_complete = False
if "application_summary" not in st.session_state:
    st.session_state.application_summary = ""

# Sidebar: Upload Resume
st.sidebar.header("📤 Upload Resume")
resume = st.sidebar.file_uploader("Upload a PDF Resume", type=["pdf"])

if resume:
    st.sidebar.success("✅ Resume uploaded")
    resume_text = extract_text_from_pdf(resume)
    extracted = extract_info_from_cv(resume_text)
    for k in application_info:
        if extracted[k]:
            application_info[k] = extracted[k]
    st.sidebar.info("📄 Extracted Info:")
    for key, value in extracted.items():
        if value:
            st.sidebar.markdown(f"**{key.title()}:** {value}")

# Reset
if st.sidebar.button("🔄 Reset"):
    st.session_state.chat_history.clear()
    st.session_state.goal_complete = False
    st.session_state.application_summary = ""
    for k in application_info:
        application_info[k] = None
    st.experimental_rerun()

# Chat Input
user_input = st.chat_input("Type your details or ask a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    extract_application_info(user_input)
    response = chat.send_message(user_input)
    ai_reply = response.text
    st.session_state.chat_history.append(("bot", ai_reply))

    goal_status = check_goal_status()
    st.session_state.chat_history.append(("status", goal_status))

    if "you're ready" in goal_status.lower():
        st.session_state.goal_complete = True
        summary = (
            f"✅ Name: {application_info['name']}\n"
            f"📧 Email: {application_info['email']}\n"
            f"🛠️ Skills: {application_info['skills']}"
        )
        st.session_state.application_summary = summary

# Chat Display
for sender, message in st.session_state.chat_history:
    if sender == "user":
        with st.chat_message("🧑"):
            st.markdown(message)
    elif sender == "bot":
        with st.chat_message("🤖"):
            st.markdown(message)
    elif sender == "status":
        with st.chat_message("📊"):
            st.info(message)

if st.session_state.goal_complete:
    st.success("🎉 All required info collected! You're ready to apply!")

if st.session_state.application_summary:
    st.download_button(
        label="📥 Download Application Summary",
        data=st.session_state.application_summary,
        file_name="application_summary.txt",
        mime="text/plain"
    )
