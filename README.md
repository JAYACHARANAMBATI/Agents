# Agents Project

A collection of intelligent agent implementations in Python, including:
- **Simple Reflex Agent** (visualized with Matplotlib)
- **Learning Agent** (Q-learning Snake game with Pygame)
- **Goal-Based Agent** (Gemini-powered job application assistant with Streamlit)

---

## Folder Structure

```
Agents/
│
├── Goal-Based/
│   ├── .env
│   ├── goal_based_agent.py
│   └── goal_based_agent_v3.py
│
├── Learning_agent.py
├── Simple_Reflex_Agent.py
└── README.md
```

---

## Agents Overview

### 1. Simple Reflex Agent

- **File:** `Simple_Reflex_Agent.py`
- **Description:** Simulates a vacuum cleaner agent in a 2x2 grid. Visualizes the agent's actions using Matplotlib.

#### Run:
```bash
python Simple_Reflex_Agent.py
```

---

### 2. Learning Agent (Q-learning Snake)

- **File:** `Learning_agent.py`
- **Description:** Implements a simple Q-learning agent to play a Snake game on a 5x5 grid using Pygame.

#### Requirements:
- `pygame`
- `numpy`

#### Run:
```bash
pip install pygame numpy
python Learning_agent.py
```

---

### 3. Goal-Based Agent (Job Application Assistant)

- **Folder:** `Goal-Based/`
- **Files:** `goal_based_agent.py`, `goal_based_agent_v3.py`
- **Description:** Uses Google Gemini API to help users collect and verify job application details (name, email, skills) via chat or PDF resume upload. Built with Streamlit.

#### Requirements:
- `streamlit`
- `python-dotenv`
- `PyMuPDF`
- `google-generativeai`

#### Setup:
1. **Install dependencies:**
    ```bash
    pip install streamlit python-dotenv pymupdf google-generativeai
    ```
2. **Set up your `.env` file in `Goal-Based/` with your Google API key:**
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```
3. **Run the Streamlit app:**
    ```bash
    cd Goal-Based
    streamlit run goal_based_agent_v3.py
    ```

---


## Author

Ambati Jaya Charan
