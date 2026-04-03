def generate_response(text: str, intent: str):

    if intent == "depression":
        return "I'm really sorry you're feeling this way. Want to talk about it?"
    elif intent == "anxiety":
        return "It sounds like you're feeling anxious. I'm here to listen."
    else:
        return "I'm here for you. Tell me what's on your mind."
