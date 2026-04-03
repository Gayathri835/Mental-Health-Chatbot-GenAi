from services.llm_router import call_ollama

def generate_reply(text: str, intent: str):

    system_prompt = """
    You are a compassionate mental health assistant.
    Be empathetic, non-judgmental, and supportive.
    Do not give medical diagnosis.
    """

    prompt = f"{system_prompt}\nUser: {text}\nAssistant:"

    response = call_ollama(prompt)

    return response
