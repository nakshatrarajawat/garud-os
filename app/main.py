from config import APP_NAME, VERSION


def main():
    print(f"\n=== Welcome to {APP_NAME} v{VERSION} ===")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Garud: Goodbye!")
            break

        print(f"Garud: I heard you say: {user_input}")


if __name__ == "__main__":
    main()
