from gamestats import *
from guesser import *  
import time 
import os 
from itertools import zip_longest

def create_info_list(guesses_remaining, correct_letters, incorrect_letters):
    info_lst = [""]
    info_lst += ["You have: " + str(guesses_remaining) + "guesses remaining"]
    info_lst += ["These letters are in the secret phrase: " + str(correct_letters)]
    info_lst += ["These letters are NOT in the secret phrase: " + str(incorrect_letters)]
    for i in range(15):
        info_lst += [""]
    return info_lst

def create_ascii_list(ascii_file_path):
    ascii_lst = []
    x = open(ascii_file_path)
    for line in x:
        line = line[:-1]
        ascii_lst += [line]
    return ascii_lst 

def user_interface():
    """controls the flow of the game and the user inputs"""
    stats = GameStats()
    
    hidden_phrase, phrase = phrase_collector()
    hide_message()
    info_list = create_info_list(stats.remaining_guesses, stats.right_guesses, stats.wrong_guesses)
    ascii_list = create_ascii_list("ascii_art/art_hangman_0.txt")
    #display_menu()
    for info_line, ascii_line in zip_longest(info_list, ascii_list):
        print(f"{ascii_line:<15}{info_line}")
        
    while True:
        if stats.health <= 0:
            print("Game Over\nThe secret phrase was: " + phrase)
            x = end_game_sequence()
        if "#" not in hidden_phrase:
            print("CONGRATULATIONS\nYou Won")
            x = end_game_sequence()
            if x:
                hidden_phrase, phrase = phrase_collector()
                hide_message()
                stats = GameStats()
                display_menu()
            else:
                break
                     
        print("The hidden phrase: " + hidden_phrase)
        print("\n")
        x = input("Please select menu option: ")
        
        if x == "1":
            guess = input("Please guess a letter: ").lower()
            if guess in stats.wrong_guesses:
                print("You have already guessed " + guess +"\n Please try again!")
            else:
                indexes = checker(phrase, guess)
                if indexes == []:
                    print(guess + " is not in the secret phrase")
                    stats.wrong_guess(guess)
                else:
                    print(guess + " is in the secret phrase")
                    stats.correct_guess(guess)
                    hidden_phrase = replace(indexes, hidden_phrase, guess)
        
        elif x == "2":
            guessed_phrase = input("Please guess the phrase: ").lower()
            if guessed_phrase == phrase:
                print("CONGRATULATIONS\nYou Won")
                x = end_game_sequence()
                if x:
                    hidden_phrase, phrase = phrase_collector()
                    hide_message()
                    stats = GameStats()
                    display_menu()
                else:
                    print("Thank you for playing")
                    break
            else:
                print("You guessed incorrectly: "  + guessed_phrase + "is not the secret phrase\n"
                "The secret phrase was: " + phrase)
                x = end_game_sequence
                if x:
                    hidden_phrase, phrase = phrase_collector()
                    hide_message()
                    stats = GameStats()
                    display_menu()
                else:
                    print("Thank you for playing\nBetter luck next time")
                    break
            
        elif x == "3":
            print("Incorrected guesses:", stats.wrong_guesses)
        
        elif x== "4":
            print("Correct guesses:", stats.right_guesses)
        
        elif x == "5":
            print("You have " + str(stats.health) + " percent health remaining")
        
        elif x == "6":
            print("You have " + str(stats.remaining_guesses) + " remaining")

        elif x == "7":
            print("Thank you for playing")
            break
        
        else:
            print("Invalid Input. Please Try Again")
        
def end_game_sequence():
    """Takes user input for if they want to play another game and returns a boolean True/False"""
    x = input("Do you want to play again (y/n) ").lower()
    if x == "y":
        return True
    else:
        return False

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
    
        
def display_menu():
    """displays the options for the user to pick from for game"""
    print("(1) Guess a letter ")
    print("(2) Guess a the complete phrase ")
    print("(3) Display incorrect guesses ")
    print("(4) Display corrected guesses ")
    print("(5) Display Health Stats ")
    print("(6) Display Number of Remaining Guesses")
    print("(7) Quit")
    
user_interface()