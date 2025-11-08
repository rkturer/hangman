from gamestats import *
from guesser import *  
import time 
import os 
from itertools import zip_longest

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


def find_ascii_path(stats):
    """creates a list that stores filepath for each ascii art and returns the correct path based on number of remaining gueses"""
    lst_ascii = ["ascii_art/art_hangman_0.txt", "ascii_art/art_hangman_1.txt", "ascii_art/art_hangman_2.txt", 
                 "ascii_art/art_hangman_3.txt", "ascii_art/art_hangman_4.txt", "ascii_art/art_hangman_5.txt",
                 "ascii_art/art_hangman_6.txt"]
    index = -(stats.remaining_guesses) -1
    return lst_ascii[index]

def win_ascii():
    return "ascii_art/art_hangman_win.txt"

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
    
    
user_interface()

