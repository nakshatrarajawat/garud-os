import ollama


MODEL = "llama3.2:3b"


def generate_response(user_input):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]