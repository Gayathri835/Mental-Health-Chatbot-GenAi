from fastapi import APIRouter
from models.schemas import ChatRequest
from services.classifier import classify_intent
from services.responder import generate_response
from services.safety import check_crisis

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    user_input = request.message

    intent = classify_intent(user_input)
    is_crisis = check_crisis(intent)

    if is_crisis:
        return {
            "response": "I’m really sorry you're feeling this way. I'm connecting you to help.",
            "escalation": True
        }

    response = generate_response(user_input, intent)

    return {
        "response": response,
        "intent": intent,
        "escalation": False
    }
