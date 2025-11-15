from gamestats import *

class Ascii:
    """handles everything related to the ascii art"""
    def __init__(self, lst):
        """initalizes phase to path to ascii art and lst a list of all the file paths"""
        self.phase = lst[0]
        self.lst = lst


    def update_phase(self, stats):
        """updates phase to filepath of appropraite ascii art"""
        index =  -(stats.remaining_guesses) -2
        self.phase = self.lst[index]

    def lose_phase(self):
        """assigns phase to filepath of lose ascii art"""
        self.phase = self.lst[-2]
    
    def win_phase(self):
        """assigns phase to filepath of win ascii art"""
        self.phase = self.lst[-1]

    def create_ascii_list(self):
        """opens the ascii file, reads it, assigns each line as an element to the ascii_list variable. Returns ascii_list"""
        with open(self.phase, "r") as x:
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





