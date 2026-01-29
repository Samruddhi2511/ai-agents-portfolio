from agent import run_agent_logic

def chat():
    print("AI started. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = run_agent_logic(user_input)
        print("AI:", response)


if __name__ == "__main__":
    chat()
