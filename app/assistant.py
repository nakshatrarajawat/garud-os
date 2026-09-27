def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    elif "what can you do" in user_input:
        return "Right now I can chat with you. Soon I'll have memory, tools, and AI."

    elif "your name" in user_input:
        return "I'm Garud."

    else:
        return "I don't know how to answer that yet."