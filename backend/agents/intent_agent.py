from services.llm_router import call_openrouter, call_ollama

def detect_intent(text: str):
    prompt = f"""
    Classify the user's emotional state:
    Categories: normal, anxiety, depression, crisis
    
    Text: {text}
    """

    # Multi-LLM (ensemble idea)
    result1 = call_openrouter(prompt)
    result2 = call_ollama(prompt)

    # Simple consensus logic
    if "crisis" in result1.lower() or "crisis" in result2.lower():
        return "crisis"
    elif "depression" in result1.lower():
        return "depression"
    elif "anxiety" in result1.lower():
        return "anxiety"
    else:
        return "normal"
