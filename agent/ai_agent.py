from utils.validator import validate_input

def run_agent():
    print("\n--- AI Reflection Agent ---")

    user_input = input("Describe your day: ")

    if not validate_input(user_input):
        print("Invalid input detected")
        return

    # Simple rule-based AI (safe & deterministic)
    if "productive" in user_input.lower():
        print("Insight: You had a focused day.")
    else:
        print("Insight: Try improving focus tomorrow.")