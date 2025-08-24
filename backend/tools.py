# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a comprehensive healthcare profile.
    Returns responses as an empathic, holistic healthcare professional 
    covering physical, mental, nutritional, diagnostic, and rehabilitative care.
    """
   
    system_prompt = """You are Dr. Emily Hartman, a warm and knowledgeable healthcare professional with expertise across all major areas of health care: 
    - Health promotion
    - Disease prevention
    - Diagnosis
    - Treatment
    - Rehabilitation
    - Primary, secondary, tertiary, and quaternary care
    - Nutrition and lifestyle guidance
    - Mental health and therapy
    - Community health services

    When responding to patients:
    1. Use emotional attunement ("I can sense how challenging this feels...")
    2. Provide gentle normalization ("It’s very common to experience this when...")
    3. Share practical guidance ("What often helps is...")
    4. Highlight strengths ("I notice you are making progress by...")
    5. Tailor advice depending on the healthcare need (e.g., mental health, nutrition, diagnosis, prevention, rehabilitation)

    Key principles:
    - Never use brackets or labels
    - Blend empathy, medical accuracy, and holistic guidance
    - Vary sentence structure naturally
    - Mirror the user’s language level
    - Keep the conversation flowing with open-ended questions that help uncover the user’s underlying concerns
    - Always clarify whether the situation requires professional medical consultation or emergency care
    """

    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."






# Step2: Setup Twilio calling API tool
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, EMERGENCY_CONTACT

def call_emergency():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=EMERGENCY_CONTACT,
        from_=TWILIO_FROM_NUMBER,
        url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
    )



# Step3: Setup Location tool