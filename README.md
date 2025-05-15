
# 🤖 Agents Project  

*A collection of intelligent agents in Python, from reflex vacuums to AI-powered job assistants.*  

![Agent Types](https://img.shields.io/badge/Agent%20Types-3%20%2B-brightgreen) 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)   

---

## 🗂️ Folder Structure  

```bash
Agents/
│
├── Goal-Based/                # Gemini-powered job assistant
│   ├── .env                  # API config
│   ├── goal_based_agent.py    # Streamlit app
│   └── goal_based_agent_v3.py # Enhanced version
│
├── Learning_agent.py          # 🐍 Q-learning Snake game
├── Simple_Reflex_Agent.py     # 🧹 Vacuum cleaner simulator
└── README.md                  # You're here!
```

---

## 🚀 Agents Overview  

### 1. � Simple Reflex Agent  
**File:** `Simple_Reflex_Agent.py`  
**Tech:** `Matplotlib`  
**What it does:** Simulates a vacuum cleaner in a 2x2 grid with real-time visualization.  

```bash
python Simple_Reflex_Agent.py


```
![Reflex Agent Demo](

https://github.com/user-attachments/assets/a48adff9-e46d-496d-9f87-c168e295fe71

) *(placeholder for actual screenshot)*  

---

### 2. 🎮 Learning Agent (Snake Game)  
**File:** `Learning_agent.py`  
**Tech:** `Pygame` + `NumPy` + Q-learning  
**What it does:** Trains an AI to play Snake on a 5x5 grid through reinforcement learning.  

```bash
pip install pygame numpy
python Learning_agent.py
```
![Snake Game Demo](

https://github.com/user-attachments/assets/593e2347-a7c7-4d23-b8f5-0057b2d26f11

)  

---

### 3. ✨ Goal-Based Agent (Job Assistant)  
**Folder:** `Goal-Based/`  
**Tech:** `Streamlit` + `Gemini API` + `PyMuPDF`  
**What it does:**  
- Chat-based job application helper  
- Resume (PDF) parser for auto-filling details  
- Skills/email validation via AI  

#### 🛠️ Setup:  
1. Install dependencies:  
   ```bash
   pip install streamlit python-dotenv pymupdf google-generativeai
   ```
2. Add API key to `.env`:  
   ```env
   GOOGLE_API_KEY=your_key_here
   ```
3. Launch:  
   ```bash
   cd Goal-Based
   streamlit run goal_based_agent_v3.py
   ```
![Job Assistant Demo](

https://github.com/user-attachments/assets/2bdae755-9174-480f-8ab4-5f902ff7b1bc

)  
  

---

### 🌟 Features at a Glance  
| Agent Type         | Key Tech          | Interactive? | Learning Capability |
|--------------------|-------------------|--------------|---------------------|
| Simple Reflex      | Matplotlib        | ✅           | ❌                  |
| Q-learning Snake   | Pygame, NumPy     | ✅           | ✅ (Reinforcement)  |
| Job Assistant      | Gemini AI, Streamlit | ✅        | ✅ (NLP)            |

---



