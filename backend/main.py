from fastapi import FastAPI
from models.schemas import ChatRequest
from agents.intent_agent import detect_intent
from agents.safety_agent import check_risk
from agents.response_agent import generate_reply
from services.twilio_service import trigger_alert

app = FastAPI()

@app.post("/chat")
async def chat(request: ChatRequest):
    user_input = request.message

    # 1. Intent Detection (Multi-LLM)
    intent = detect_intent(user_input)

    # 2. Safety Check
    risk = check_risk(user_input, intent)

    if risk == "high":
        trigger_alert(user_input)
        return {
            "response": "I'm really sorry you're feeling this way. I'm connecting you to immediate support.",
            "escalation": True
        }

    # 3. Generate Response (LLM)
    reply = generate_reply(user_input, intent)

    return {
        "response": reply,
        "intent": intent,
        "risk": risk,
        "escalation": False
    }
