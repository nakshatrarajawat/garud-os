from app.memory import remember, recall
def get_response(user_input):
    user_input_lower = user_input.lower().strip()

    if user_input_lower.startswith("remember "):
        information = user_input[9:].strip()

        if "=" in information:
            key, value = information.split("=", 1)
            remember(key.strip(), value.strip())
            return f"I'll remember that {key.strip()} is {value.strip()}."

        return "Use this format: remember name = Nakshatra"

    elif user_input_lower.startswith("recall "):
        key = user_input[7:].strip()
        value = recall(key)

        if value is None:
            return "I don't remember that yet."

        return f"{key} is {value}."

    elif user_input_lower in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "what can you do" in user_input_lower:
        return "I can chat, remember information, and recall it."

    elif "your name" in user_input_lower:
        return "I'm Garud."

    else:
        return "I don't know how to answer that yet."
