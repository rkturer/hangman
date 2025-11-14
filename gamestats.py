#Rachel Turer --> Hangman Game using OOP
class GameStats:
    


    def __init__(self):
        """initalizes the health and remaining guesses for the user"""
        self.remaining_guesses = 6 
        self.total_guesses = 0
        self.wrong_guesses = []
        self.right_guesses = []
        self.game = "hangman"
        self.result = ""
        self.full_guess = False
        self.win = False
    
    def wrong_guess(self, guess):
        """removes health and guesses for a wrong guess"""
        self.remaining_guesses -=1
        self.wrong_guesses += guess
        self.total_guesses +=1
    
    def has_guessed(self, guess):
        """takes parameters as guess nad stats objects and checks if the guess is already"""
        if guess in self.wrong_guesses or guess in self.right_guesses: 
            return True
    
    def correct_guess(self, guess):
        """updates attributes occordinly for correct guesses"""
        self.right_guesses += guess
        self.total_guesses +=1
    
    def __repr__(self):
        return "You have guessed these letters correctly: " + str(self.right_guesses) + "\nYou have guessed these letters incorrectly: "  + str(self.wrong_guesses) + "\nYou guessed " + str(self.total_guesses) + "  times\nYou have " + str(self.remaining_guesses) + " guesses left"
    
    
    
    