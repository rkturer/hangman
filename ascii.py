
def create_ascii_list(ascii_file_path):
    ascii_lst = []
    x = open(ascii_file_path)
    for line in x:
        line = line[:-1]
        ascii_lst += [line]
    return ascii_lst 

def find_ascii_path(stats):
    """creates a list that stores filepath for each ascii art and returns the correct path based on number of remaining gueses"""
    lst_ascii = ["ascii_art/art_hangman_0.txt", "ascii_art/art_hangman_1.txt", "ascii_art/art_hangman_2.txt", 
                 "ascii_art/art_hangman_3.txt", "ascii_art/art_hangman_4.txt", "ascii_art/art_hangman_5.txt",
                 "ascii_art/art_hangman_6.txt"]
    index = -(stats.remaining_guesses) -1
    return lst_ascii[index]

def win_ascii():
    return "ascii_art/art_hangman_win.txt"




