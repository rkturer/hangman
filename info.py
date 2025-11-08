import time 
from guesser import formatter 

def create_info_list(stats, dynamic_phrase, hidden_phrase):
    info_lst = [""]
    info_lst += [f"You have {stats.remaining_guesses} guesses remaining"]
    info_lst += [f"These letters are in the secret phrase: {stats.right_guesses}"]
    info_lst += [f"These letters are NOT in the secret phrase: {stats.wrong_guesses}"]
    for i in range(3):
        info_lst += [""] 
    info_lst += [f"{dynamic_phrase}"]
    for i in range(3):
        info_lst += [""] 
    info_lst += [f"The hidden phrase is: {hidden_phrase}"]
    for i in range(7):
        info_lst += [""] 

    return info_lst

def phrase_collector():
    """takes the phrase from the user and hides it using the formatter function. Returns the hidden phrase and the original phrase"""
    x = input("Please enter your secret phrase: ").lower()
    hidden_phrase = formatter(x)
    return hidden_phrase, x 


def hide_message():
    """takes no parameters and hides the secret message after a 3 second delay"""
    print("Hiding the secret message...")
    time.sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    