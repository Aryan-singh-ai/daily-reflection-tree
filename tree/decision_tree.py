from tree.tree_logic import evaluate_day

def run_tree():
    print("\n--- Daily Reflection Tree ---")

    task_done = input("Did you complete your main task? (yes/no): ")
    productivity = input("Were you productive? (yes/no): ")

    result = evaluate_day(task_done, productivity)
    print("\nResult:", result)