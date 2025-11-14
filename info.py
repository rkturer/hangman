#Rachel Turer --> Hangman Game using OOP
import random
from gamestats import *
class Phrase:

    """handles everything regarding the hidden phrase """

    def __init__(self):
        """initalizes the phrase, hiddenphrase, random list of phrases, and the textfile path for the random phrases text, and the extra phrase"""
        self.phrase = "" 
        self.hidden_phrase = ""
        self.random_list = []
        self.random_txt_file = "hangman_phrases.txt"
        self.extra_phrase = ""
        self.num_chars = 0
        self.is_random = False

    def formatter(self):
        """takes the secret phrase as an input and reformats it to keep the shape but hide the letters"""
        components = self.phrase.split()
        for i in range(len(components)-1):
            self.hidden_phrase = self.hidden_phrase + len(components[i]) * "#"
            self.hidden_phrase += " "
        self.hidden_phrase += len(components[-1]) * "#"
        self.find_num_chars()
    
    def checker(self, char):
        """takes the phrase and a character and returns a list of indexes where the character occurs in the phrase""" 
        indexes = []
        if char in self.phrase:
            for i in range(len(self.phrase)):
                if self.phrase[i] == char:
                    indexes += [i] 
        return indexes 

    def find_num_chars(self):
        components = self.phrase.split()
        for component in components:
            self.num_chars += len(component)

    def replace(self, indexes, char):
        """takes a list of indexes, a str character and hidden phrase and changes the hidden phrase with the appropriate letters replacing the #"""
        if indexes == []:
            self.hidden_phrase = self.hidden_phrase
        else:
            if indexes[-1] == len(self.hidden_phrase)-1:
                self.hidden_phrase = self.hidden_phrase[:-1] + char 
                indexes = indexes[:-1]
            for i in indexes:
                self.hidden_phrase = self.hidden_phrase[:i] + char + self.hidden_phrase[i+1:]

    def phrase_collector(self):
        """takes the phrase from the user and hides it using the formatter function. Returns the hidden phrase and the original phrase"""            
        self.phrase = input("Please enter your secret phrase: ").lower()

    def create_list_of_phrases(self):
        """takes a file path as input and reads everyline in file and puts each line into a list. returns the list"""            
        file = open(self.random_txt_file)
    
        for line in file:
            line = line[:-1] #remove the \n 
            self.random_list += [line.lower()]
            
        file.close()

    def random_phrase(self):
        """takes a list of strings as an input and randomly selects and returns a string"""
        self.is_random = True
        self.phrase = random.choice(self.random_list)
    
    

    def create_info_list(self, stats):
        """creates a list of values the same length as the ascii art for the display function"""
        info_lst = [""]
        info_lst += [f"You have {stats.remaining_guesses} guesses remaining"]
        info_lst += [f"These letters are in the secret phrase: {stats.right_guesses}"]            
        info_lst += [f"These letters are NOT in the secret phrase: {stats.wrong_guesses}"]
        for i in range(3):
            info_lst += [""] 
        info_lst += [f"{self.extra_phrase}"]
        for i in range(3):
            info_lst += [""] 
        info_lst += [f"The hidden phrase is: {self.hidden_phrase}"]
        for i in range(7):
            info_lst += [""] 

        return info_lst
