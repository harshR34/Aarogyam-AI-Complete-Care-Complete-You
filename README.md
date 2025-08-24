# Aarogyam AI: Holistic Healthcare Chatbot

Aarogyam AI is an advanced AI-powered healthcare assistant providing empathetic guidance, nearby doctor recommendations, and emergency support. It combines **Ollama (MedGemma)** for local, context-aware responses and **Groq (ChatGroq)** for fast, scalable reasoning. The backend is built with **FastAPI**, and the frontend uses **Streamlit** for interactive user experience.

---

## Features

- Conversational AI for **general healthcare** queries (nutrition, prevention, mental health, rehab).  
- **Nearby doctor & clinic recommendations** based on user location.  
- **Emergency call support** using Twilio for life-threatening situations.  
- Hybrid AI architecture combining **Ollama + Groq** for privacy, speed, and reliability.  
- Stores chat history by date for easy retrieval.  

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/aarogyam-ai.git
cd aarogyam-ai


python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

# --- Backend dependencies ---
pip install fastapi
pip install uvicorn
pip install requests
pip install python-dotenv

# --- Frontend dependencies ---
pip install streamlit

# --- AI / LLM dependencies ---
pip install groq
pip install langchain
pip install langchain-groq
pip install langchain-ollama
pip install langgraph

# --- Twilio for emergency call service ---
pip install twilio

# --- Optional (for async, performance, etc.) ---
pip install httpx
pip install aiohttp



---

If you want, I can also **add a “Project Architecture Diagram” and “Tech Stack” section** to this README so it looks **more professional for GitHub**.  

Do you want me to do that next?
