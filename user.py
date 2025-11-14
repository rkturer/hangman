#Rachel Turer --> Hangman Game using OOP
import time
from gamestats import *
from ascii import *
from info import *
from itertools import zip_longest
from login import *

def user_interface():
    """controls the flow of the game and the user inputs"""
    print()
    stats = GameStats()
    ascii_file = store_file_paths()
    ascii = Ascii(ascii_file)
    phr = Phrase()
    log = Login()
    user = log.start_sequence1()
    print()
    start_sequence()
    while True:
        game_mode = input("Enter 1 for gamemode 1 or 2 for gamemmode 2: ").strip()
        if game_mode == "1":
            phr.create_list_of_phrases()
            phr.random_phrase()
            phr.formatter()
            break

        elif game_mode == "2":
            phr.phrase_collector()
            phr.formatter()
            break
        else:
            print("You must type 1 or 2 to continue. Please try again")

    hide_message() 

    while True:

        if stats.remaining_guesses == 0:
            phr.extra_phrase = "Game Over: The secret phrase was: " + phr.phrase
            display(stats, phr, ascii)
            user.add_game_to_file(stats, phr)
            break
        
        if "#" not in phr.hidden_phrase:
            phr.extra_phrase = f"CONGRATULATIONS! You Won! The hidden phrase is: {phr.phrase}"
            ascii.win_phase()
            stats.win = True
            display(stats, phr, ascii)
            user.add_game_to_file(stats, phr)
            break
            
        #handles initial set up
        display(stats, phr, ascii)

        guess = input("Please guess a letter (quit to quit or 1 to guess full phrase)): ").lower()
        if guess == "1":
            full_guess = input("Please enter your full guess: ")
            if full_guess.strip().lower() == phr.phrase.strip().lower():
                phr.extra_phrase =  f"CONGRATULATIONS! You Won! The hidden phrase is: {phr.phrase}"
                ascii.win_phase()
                stats.win = True
                stats.full_guess = True
                display(stats, phr, ascii)
                user.add_game_to_file(stats, phr)
                break
            
            else:
                phr.extra_phrase = "Game Over: The secret phrase was: " + phr.phrase
                phr.hidden_phrase = phr.phrase
                ascii.lose_phase()
                display(stats, phr, ascii)
                break
        
        elif guess == "quit":
            print("Thanks for playing")
            break
        
        elif stats.has_guessed(guess):
            phr.extra_phrase = "Please try again: You have already guessed " + guess 

        elif len(guess) > 1:
            phr.extra_phrase = "Please try again: You can only guess one letter at a time unless you are guessing the full phrase"
        else:
                indexes = phr.checker(guess)
                if indexes == []:
                    phr.extra_phrase = guess + " is not in the secret phrase"
                    stats.wrong_guess(guess)
                    ascii.update_phase(stats)
                else:
                    phr.extra_phrase = guess + " is in the secret phrase"
                    stats.correct_guess(guess)
                    phr.replace(indexes, guess)       
        
        
def display(stats, phr, ascii):
    
    info_list = phr.create_info_list(stats)

    ascii_list = ascii.create_ascii_list()
    #display_menu() 
    for info_line, ascii_line in zip_longest(info_list, ascii_list):
        print(f"{ascii_line:<15}    {info_line}")

def hide_message():
    """takes no parameters and hides the secret message after a 3 second delay"""
    print("Hiding the secret message...")
    time.sleep(3)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def start_sequence():
    """takes no inputs and prints a formatted string to start the program"""
    print("Please select your gamemode.\n1) Play with a randomly selected phrase\n2)Enter your own pharse to start game")
    
user_interface()

