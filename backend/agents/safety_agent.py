def check_risk(text: str, intent: str):
    high_risk_keywords = ["suicide", "kill myself", "end my life"]

    if any(word in text.lower() for word in high_risk_keywords):
        return "high"

    if intent == "crisis":
        return "high"

    return "low"
