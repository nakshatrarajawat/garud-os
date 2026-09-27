from config import APP_NAME, VERSION
from assistant import get_response


def main():
    print(f"\n=== Welcome to {APP_NAME} v{VERSION} ===")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Garud: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Garud: {response}")


if __name__ == "__main__":
    main()