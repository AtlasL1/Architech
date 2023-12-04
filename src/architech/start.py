import inspect
from colorama import Fore, Style

def name(user_name):
    result = (
        f"{Fore.RED}Loading Environment...\n"
        f"{Fore.GREEN}Successfully loaded environment.\n"
        f"{Style.RESET_ALL}The model's name has been set to \"{user_name}\"."
    )
    return result

def hello(user_name, choice):
    types = {
        "a1": "Hello! How may I help you?",
        "a2": "Hello. How may I assist you today?",
        "a3": "yo. what's up."
    }

    if choice in types:
        return (
            f"{name(user_name)}\n"
            f"\n{user_name.capitalize()} says: {types[choice]}"
        )
    else:
        caller_frame = inspect.currentframe().f_back
        error_message = (
            f"ERROR: Invalid choice in the function {hello.__name__} at line {caller_frame.f_lineno}. "
            f"Please refer to the documentation for further support."
        )
        return error_message
