import streamlit as st
import requests
import base64

BACKEND_URL = "http://localhost:8000/ask"
HISTORY_URL = "http://localhost:8000/chat_history"

# Set up the page
st.set_page_config(page_title='Aarogyam AI', layout='wide')

# Inject custom CSS
st.markdown("""
    <style>
    .fixed-title {
        position: fixed;
        top: 30px;
        left: 0;
        width: 100%;
        background-color: #0e1117;
        padding: 1.5rem 2rem;
        z-index: 1000;
    }
    .main > div {
        padding-top: 130px;
    }
    .chat-container {
        margin-top:55px
    }
    </style>
""", unsafe_allow_html=True)

# Read and convert the image to Base64
with open(r"logo_chatbot.png", "rb") as img_file:
    logo_base64 = base64.b64encode(img_file.read()).decode()

# Display logo + title + button
st.markdown(
    f"""
    <div class="fixed-title" style="display:flex;align-items:center;justify-content:space-between;">
        <div style="display:flex;align-items:center;gap:12px;">
            <img src="data:image/png;base64,{logo_base64}" 
                 alt="chatbot Logo" 
                 style="width:50px;height:50px;border-radius:50%;object-fit:cover;">
            <h1 style="margin:0;font-size:28px;">Aarogyam AI: Complete Care, Complete You</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # AI Agent request
    response = requests.post(BACKEND_URL, json={"message": user_input})
    st.session_state.chat_history.append({
        "role": "assistant", 
        "content": f'{response.json()["response"]} WITH TOOL: [{response.json()["tool_called"]}]'
    })

# Display chat
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    st.markdown('</div>', unsafe_allow_html=True)


#  <a href="{HISTORY_URL}" target="_blank" style="text-decoration:none;">
#             <button style="background-color:#4CAF50;color:white;padding:8px 16px;
#                            border:none;border-radius:8px;font-size:16px;cursor:pointer;">
#                 📜 View Chat History
#             </button>
#         </a>

