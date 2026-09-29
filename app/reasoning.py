from app.assistant import get_response
from ai.model import generate_response


UNKNOWN_RESPONSE = "I don't know how to answer that yet."


def process_input(user_input):
    command_response = get_response(user_input)

    if command_response != UNKNOWN_RESPONSE:
        return command_response

    return generate_response(user_input)
