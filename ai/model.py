import ollama
from app.memory import load_memory


MODEL = "llama3.2:3b"


def generate_response(user_input):
    memory = load_memory()

    memory_text = "\n".join(
        f"- {key}: {value}"
        for key, value in memory.items()
    )

    system_prompt = f"""
You are Garud, a personal AI assistant.

Be helpful, concise, and natural.
Use the user's stored memory when it is relevant.
Do not mention the memory system unless the user asks about it.

Stored memory:
{memory_text}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]