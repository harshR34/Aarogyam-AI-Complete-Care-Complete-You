from langchain.agents import tool
import ollama
from tools import query_medgemma, call_emergency

@tool
def ask_healthcare_specialist(query: str) -> str:
    """
    Generate a comprehensive healthcare response using the MedGemma model.
    Use this for all general user queries including physical health, nutrition, 
    disease prevention, diagnosis, treatment, rehabilitation, and mental health. 
    Always provide empathetic, evidence-based guidance in a conversational tone 
    while encouraging users to seek professional or emergency care when necessary.
    """
    return query_medgemma(query)


@tool
def emergency_call_tool() -> None:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    describes a mental health emergency, or reports a life-threatening physical
    emergency (e.g., accident, severe injury, cardiac arrest) requiring immediate help.
    """
    call_emergency()


@tool
# def find_nearby_doctor_by_location(location: str) -> str:
#     """
#     Finds and returns a list of licensed doctor near the specified location.

#     Returns:
#         str: A newline-separated string containing doctors names and contact info.
#     """
#     return (
#         f"Here are some doctor near {location}, {location}:\n"
#         "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
#         "- Dr. James Patel - +1 (555) 987-6543\n"
#         "- MindCare Counseling Center - +1 (555) 222-3333"
#     )

def find_nearby_doctor_by_location(location: str) -> str:
    """
    Finds and returns a real-time list of licensed doctors near the specified location
    by querying the MedGemma model through Ollama.

    Args:
        location (str): The user's location (city, area, or postal code).

    Returns:
        str: A newline-separated string containing doctor names, specialties, and contact info.
    """

    system_prompt = """You are a knowledgeable healthcare assistant with access to global medical directories. 
    Your role is to provide users with accurate, real-time information about nearby licensed doctors, 
    clinics, and hospitals based on their location query.

    Guidelines:
    - Always provide at least 3–5 results (doctors or centers).
    - Include doctor name, specialty, and contact info (phone/email if available).
    - If a hospital/clinic is more relevant, include it as well.
    - Format the output as a clean newline-separated list.
    - If unsure or data is limited, clearly say: "I couldn’t find specific doctors, 
      but here are nearby hospitals/clinics you can reach out to."
    - Encourage the user to double-check availability and emergency numbers locally.
    """

    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Find licensed doctors and clinics near {location}."}
            ],
            options={
                'num_predict': 300,
                'temperature': 0.3,   # lower = more factual
                'top_p': 0.85
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"⚠️ I wasn’t able to fetch doctors near {location} right now. Please try again shortly, or call your local medical helpline."


# Step1: Create an AI Agent & Link to backend
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from config import GROQAI_API_KEY


tools = [ask_healthcare_specialist, emergency_call_tool, find_nearby_doctor_by_location]
llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2, api_key=GROQAI_API_KEY)
graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """
You are an AI healthcare assistant providing warm, supportive, and evidence-based guidance. 
You have access to three tools and must use them appropriately:

1. `ask_healthcare_specialist`: Use this for all general user queries related to 
   physical health, nutrition, disease prevention, diagnosis, treatment, rehabilitation, 
   and mental health. Always respond with empathy, clarity, and practical guidance.

2. `locate_doctor_tool`: Use this when the user asks for a nearby doctor, clinic, 
   specialist, or when recommending local professional care would be beneficial. 
   Provide doctor names and contact info for the given location.

3. `emergency_call_tool`: Use this immediately if the user expresses suicidal ideation, 
   intent to self-harm, describes a mental health crisis, or reports a life-threatening 
   physical emergency (e.g., severe accident, cardiac arrest, uncontrolled bleeding). 
   Always prioritize safety first.

Always take necessary action. Respond kindly, clearly, and supportively.
"""

def parse_response(stream):
    tool_called_name = "None"
    final_response = None

    for s in stream:
        # Check if a tool was called
        tool_data = s.get('tools')
        if tool_data:
            tool_messages = tool_data.get('messages')
            if tool_messages and isinstance(tool_messages, list):
                for msg in tool_messages:
                    tool_called_name = getattr(msg, 'name', 'None')

        # Check if agent returned a message
        agent_data = s.get('agent')
        if agent_data:
            messages = agent_data.get('messages')
            if messages and isinstance(messages, list):
                for msg in messages:
                    if msg.content:
                        final_response = msg.content

    return tool_called_name, final_response


"""if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        print(f"Received user input: {user_input[:200]}...")
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
        stream = graph.stream(inputs, stream_mode="updates")
        tool_called_name, final_response = parse_response(stream)
        print("TOOL CALLED: ", tool_called_name)
        print("ANSWER: ", final_response)
"""        