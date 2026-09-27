from app.assistant import get_response
from ai.model import generate_response


def process_input(user_input):
    ai_response = generate_response(user_input)

    if ai_response:
        return ai_response

    return get_response(user_input)
