# Architech
# Start.py

import inspect
from colorama import Fore, Style

global_model_name = None
global_user_name = None

def name(model_name):
    global global_model_name
    global_model_name = model_name
    result = (
        f"{Fore.RED}Loading Environment...\n"
        f"{Fore.GREEN}Successfully loaded environment.\n"
        f"{Style.RESET_ALL}The model's name has been set to \"{model_name.capitalize()}\"."
    )
    return result

def hello(choice):
    types = {
        "a1": "Hello! How may I help you?",
        "a2": "Hello. How may I assist you today?",
        "a3": "Yo. What's up.",
        "a4": "Greetings! How can I be of service?",
        "a5": "Hi! What brings you here?",
        "a6": "Salutations! Ready for a chat?",
        "a7": "Ahoy there! What brings you here?",
        "a8": "Hello! Anything exciting happening?",
        "a9": "Hey! What's the plan for today?",
        "a10": "Yo! What's the latest news?",
    }

    if choice in types:
        return (
            f"\n{global_model_name.capitalize()} says: {types[choice]}"
        )
    else:
        caller_frame = inspect.currentframe().f_back
        error_message = (
            f"\n{Fore.RED }ERROR: {Style.RESET_ALL}Invalid choice in the function {hello.__name__} at line {caller_frame.f_lineno}. "
            f"Please refer to the documentation for further support."
        )
        return error_message

def hello_output(user_name, sentence):
    global global_user_name
    global_user_name = user_name
    return (
        f"{user_name.capitalize()} says: {sentence}\n\n"
        f"{Fore.MAGENTA}Process 'START' complete."
    )

# Architech
# Onward.py

def recognition_add(sentence, response, preview=True):
    output = (
        f"\n{Fore.CYAN}{global_user_name.capitalize()}: {Style.RESET_ALL}{sentence}\n"
        f"{Fore.CYAN}{global_model_name.capitalize()}: {Style.RESET_ALL}{response}\n"
    )
    void = ''
    if preview:
        return output
    else:
        return void

def dictionary_add(word, response, preview=True):
    output = (
        f"{Fore.CYAN}{global_user_name.capitalize()}: {Style.RESET_ALL}{word}\n"
        f"{Fore.CYAN}{global_model_name.capitalize()}: {Style.RESET_ALL}{response}"
    )
    void = ''
    if preview:
        return output
    else:
        return void
