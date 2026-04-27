def evaluate_day(task_done, productivity):

    if task_done == "yes" and productivity == "yes":
        return "Excellent day"

    elif task_done == "yes" and productivity == "no":
        return "Work done but improve focus"

    elif task_done == "no":
        return "Need better planning"

    return "Invalid input"