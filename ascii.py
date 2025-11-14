from gamestats import *

class Ascii:
    def __init__(self, lst):
        self.phase = lst[0]
        self.lst = lst


    def update_phase(self, stats):
        index =  -(stats.remaining_guesses) -2
        self.phase = self.lst[index]

    def lose_phase(self):
        self.phase = self.lst[-2]
    
    def win_phase(self):
        self.phase = self.lst[-1]

    def create_ascii_list(self):
        x = open(self.phase)
        ascii_lst = []
        for line in x:
            line = line[:-1]
            ascii_lst += [line]
        return ascii_lst 

def store_file_paths():
    """creates a list that stores filepath for each ascii art and returns the correct path based on number of remaining gueses"""
    lst_ascii = ["ascii_art/art_hangman_0.txt", "ascii_art/art_hangman_1.txt", "ascii_art/art_hangman_2.txt", 
                 "ascii_art/art_hangman_3.txt", "ascii_art/art_hangman_4.txt", "ascii_art/art_hangman_5.txt",
                 "ascii_art/art_hangman_6.txt", "ascii_art/art_hangman_win.txt" ]
    
    return lst_ascii





