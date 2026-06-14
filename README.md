# 🩺 Aarogyam AI — Complete Care, Complete You

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LLM_Orchestration-yellow)
![Ollama](https://img.shields.io/badge/Ollama-MedGemma-purple)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A safety-critical AI healthcare assistant that combines **local LLM inference** (MedGemma via Ollama) with **cloud-based fast reasoning** (Llama3 via Groq), built with a focus on **responsible AI design**, empathetic responses, and real-world emergency support.

---

## 🧠 Why This Project?

Most healthcare chatbots either rely entirely on cloud APIs (raising privacy concerns) or use a single model with no fallback. Aarogyam AI explores a **hybrid LLM routing architecture** — a design pattern relevant to safe, production AI systems — where:

- **Sensitive queries** are handled **locally** via Ollama (MedGemma) for privacy preservation
- **General queries** are routed to **Groq (Llama3)** for speed and scalability
- **Emergency queries** trigger a **real-world action** (Twilio call) — demonstrating safety-critical AI pipeline design

This project was built to explore practical challenges in deploying LLMs responsibly: prompt safety, hallucination reduction, tool-use integration, and stateful multi-turn conversation.

---

## 🏗️ Architecture
URL :- 

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 Hybrid LLM Routing | Routes between Ollama (local) and Groq (cloud) based on query type |
| 🧠 Multi-turn Memory | LangChain + LangGraph maintain conversation state across sessions |
| 🏥 Doctor Finder | Real-time nearby clinic/doctor recommendations via location API |
| 🚨 Emergency Pipeline | Detects life-threatening queries → triggers Twilio emergency call |
| 💊 Domain-Constrained Prompts | System prompts engineered to prevent out-of-scope hallucinations |
| 📅 Session History | Chat history stored and retrievable by date |

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI + Uvicorn |
| LLM Orchestration | LangChain, LangGraph |
| Local LLM | Ollama (MedGemma) |
| Cloud LLM | Groq API (Llama3 / ChatGroq) |
| Emergency | Twilio Voice API |
| Environment | Python 3.11, uv package manager |

---

## 📁 Project Structure
Aarogyam-AI/

├── backend/

│   ├── chat.py          # LLM routing logic (Ollama vs Groq)

│   ├── memory.py        # LangGraph conversation state management

│   ├── doctor_search.py # Location-based doctor recommendations

│   ├── emergency.py     # Twilio emergency call trigger

│   └── prompts.py       # Domain-specific system prompts

├── frontend.py          # Streamlit UI

├── main.py              # FastAPI app entry point

├── pyproject.toml       # Dependencies (uv)

├── .env.example         # Environment variable template

└── README.md


---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/harshR34/Aarogyam-AI-Complete-Care-Complete-You.git
cd Aarogyam-AI-Complete-Care-Complete-You
pip install -r requirements.txt
```

### 2. Set Environment Variables

```bash
cp .env.example .env
# Fill in your keys:
GROQAI_API_KEY=your_groq_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=+1xxxxxxxxxx
EMERGENCY_CONTACT=+91xxxxxxxxxx
```

### 3. Start Ollama (local LLM)

```bash
ollama pull medgemma
ollama serve
```

### 4. Run Backend + Frontend

```bash
# Terminal 1 — Backend
uvicorn main:app --reload

# Terminal 2 — Frontend
streamlit run frontend.py
```

---

## 🔬 Research Notes & Design Decisions

### Prompt Safety
The system prompt explicitly constrains the model to medical domains only, rejecting off-topic requests. This reduces hallucination risk in high-stakes health contexts.

### Hybrid Routing Rationale
MedGemma (via Ollama) is a medical-domain fine-tuned model — better for nuanced clinical queries but slower. Groq's Llama3 is faster for general wellness questions. Routing between them improves both safety and latency.

### Emergency Detection
A rule-based classifier checks for keywords (chest pain, suicide, unconscious, etc.) before LLM inference — ensuring emergency response is never delayed by model latency.

### Known Limitations
- Doctor search accuracy depends on location API coverage in the user's region
- MedGemma local inference requires sufficient GPU/CPU resources
- Not a substitute for professional medical advice

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙋 Author

**Harsh Vaghela** — [GitHub](https://github.com/harshR34) | [LinkedIn](#)

*Built as part of AI/ML coursework and personal research into safe LLM deployment.*
