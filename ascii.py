
class Ascii:
    """handles all of the ascii art for the terminal"""
    def __init__(self, init_file0, init_file1, init_file2, init_file3):
        self.file0 = init_file0
        self.file1 = init_file1
        self.file2 = init_file2
        self.file3 = init_file3
        self.file2 = init_file2
        self.file1 = init_file1
        self.file2 = init_file2
        



def display_ascii(filename):
    x = open(filename, 'r')
    print(x.read())

display_ascii("ascii_art/art_hangman_0.txt")


