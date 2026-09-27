from app.config import APP_NAME, VERSION
from app.reasoning import process_input


def main():
    print(f"\n=== Welcome to {APP_NAME} v{VERSION} ===")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Garud: Goodbye!")
            break

        response = process_input(user_input)
        print(f"Garud: {response}")


if __name__ == "__main__":
    main()