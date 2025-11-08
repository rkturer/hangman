from gamestats import *
from guesser import *  
from ascii import *
from info import *
from itertools import zip_longest

def user_interface():
    """controls the flow of the game and the user inputs"""
    stats = GameStats()
    hidden_phrase, phrase = phrase_collector()
    hide_message()
    extra_phrase = ""
    while True:

        if stats.remaining_guesses == 0:
            extra_phrase = "Game Over: The secret phrase was: " + phrase
            ascii_path = find_ascii_path(stats)
            display(stats, ascii_path, extra_phrase, phrase)
            break

        if "#" not in hidden_phrase:
            extra_phrase = f"CONGRATULATIONS! You Won! The hidden phrase is: {phrase}"
            ascii_path = win_ascii()
            display(stats, ascii_path, extra_phrase, phrase)
            break
            
        #handles initial set up
        ascii_path = find_ascii_path(stats)
        display(stats, ascii_path, extra_phrase, hidden_phrase)

        guess = input("Please guess a letter (quit to quit or 1 to guess full phrase)): ").lower()
        if guess == "1":
            full_guess = input("Please enter your full guess: ")
            if full_guess.lower() == phrase:
                extra_phrase =  f"CONGRATULATIONS! You Won! The hidden phrase is: {phrase}"
                ascii_path = win_ascii()
                display(stats, ascii_path, extra_phrase, phrase)
                break
            else:
                extra_phrase = "Game Over: The secret phrase was: " + phrase
                ascii_path = find_ascii_path(stats)
                display(stats, ascii_path, extra_phrase, phrase)
                break
        
        elif guess == "quit":
            print("Thanks for playing")
            break
        
        elif guess in stats.wrong_guesses or guess in stats.right_guesses:  
            extra_phrase = "Please try again: You have already guessed " + guess 
        elif len(guess) > 1:
            extra_phrase = "Please try again: You can only guess one letter at a time unless you are guessing the full phrase"
        else:
                indexes = checker(phrase, guess)
                if indexes == []:
                    extra_phrase = guess + " is not in the secret phrase"
                    stats.wrong_guess(guess)
                else:
                    extra_phrase = guess + " is in the secret phrase"
                    stats.correct_guess(guess)
                    hidden_phrase = replace(indexes, hidden_phrase, guess)       
        
        
def display(stats, file_path, phrase, hidden_phrase):
    
    info_list = create_info_list(stats, phrase, hidden_phrase)
    ascii_list = create_ascii_list(file_path)
    #display_menu() 
    for info_line, ascii_line in zip_longest(info_list, ascii_list):
        print(f"{ascii_line:<15}    {info_line}")

    
user_interface()

