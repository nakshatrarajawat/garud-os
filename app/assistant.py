from app.memory import remember, recall


def get_response(user_input):
    user_input_lower = user_input.lower().strip()

    # Remember commands
    if user_input_lower.startswith("remember "):
        information = user_input[9:].strip()

        if "=" in information:
            key, value = information.split("=", 1)
            remember(key.strip(), value.strip())
            return f"I'll remember that {key.strip()} is {value.strip()}."

        return "Use this format: remember name = Nakshatra"

    # Direct memory assignment
    elif "=" in user_input and not user_input_lower.startswith("what"):
        key, value = user_input.split("=", 1)
        remember(key.strip(), value.strip())
        return f"I'll remember that {key.strip()} is {value.strip()}."

    # Explicit recall
    elif user_input_lower.startswith("recall "):
        key = user_input[7:].strip()
        value = recall(key)

        if value is None:
            return "I don't remember that yet."

        return f"{key} is {value}."

    # Natural-language memory questions
    elif "what is my " in user_input_lower:
        key = user_input_lower.split("what is my ", 1)[1].strip().rstrip("?")
        value = recall(key)

        if value is not None:
            return f"Your {key} is {value}."

        return "I don't have that information yet."

    elif "what's my " in user_input_lower:
        key = user_input_lower.split("what's my ", 1)[1].strip().rstrip("?")
        value = recall(key)

        if value is not None:
            return f"Your {key} is {value}."

        return "I don't have that information yet."

    # Basic commands
    elif user_input_lower in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"

    elif "what can you do" in user_input_lower:
        return "I can chat, remember information, and recall it."

    elif "your name" in user_input_lower:
        return "I'm Garud."

    return "I don't know how to answer that yet."
