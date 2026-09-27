from app.assistant import get_response


def process_input(user_input):
    response = get_response(user_input)
    return response
