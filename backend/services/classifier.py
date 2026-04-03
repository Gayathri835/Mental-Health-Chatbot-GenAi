def classify_intent(text: str):
    text = text.lower()

    if "suicide" in text or "die" in text:
        return "crisis"
    elif "sad" in text or "depressed" in text:
        return "depression"
    elif "anxious" in text or "nervous" in text:
        return "anxiety"
    else:
        return "normal"
