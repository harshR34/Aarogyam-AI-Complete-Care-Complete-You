# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import graph, SYSTEM_PROMPT, parse_response

app = FastAPI(
    title="Aarogyam AI",
    description="Holistic Healthcare Chatbot API powered by Ollama & Groq",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Aarogyam AI backend running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# In-memory chat storage
chat_history = {}

class Query(BaseModel):
    message: str

def save_chat(user_message, ai_response, tool_called):
    today = datetime.now().strftime("%Y-%m-%d")

    if today not in chat_history:
        chat_history[today] = []

    chat_history[today].append({
        "message": user_message,
        "response": ai_response,
        "tool_called": tool_called,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

@app.post("/ask", summary="Ask AI", description="Send a message to the AI and get a response.")
async def ask(query: Query):
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
    stream = graph.stream(inputs, stream_mode="updates")
    tool_called_name, final_response = parse_response(stream)

    # Save chat in history
    save_chat(query.message, final_response, tool_called_name)

    return {"response": final_response, "tool_called": tool_called_name}

@app.get("/chat_history/{date}", summary="Get Chat History (by date)", description="Fetch all chats for a specific date (YYYY-MM-DD).")
async def get_chat_history(date: str):
    return {"date": date, "chats": chat_history.get(date, [])}

@app.get("/chat_history", summary="Get All Chat History", description="Fetch all chats grouped by date.")
async def get_all_chat_history():
    return chat_history

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
