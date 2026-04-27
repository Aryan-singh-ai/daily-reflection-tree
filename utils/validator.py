from config import MAX_INPUT_LENGTH

def validate_input(user_input):
    if len(user_input) > MAX_INPUT_LENGTH:
        return False
    return True