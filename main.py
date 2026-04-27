from agent.ai_agent import run_agent
from tree.decision_tree import run_tree

def main():
    print("1. Run Decision Tree")
    print("2. Run AI Agent")

    choice = input("Choose option: ")

    if choice == "1":
        run_tree()
    elif choice == "2":
        run_agent()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()