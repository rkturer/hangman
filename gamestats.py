#Rachel Turer --> Hangman Game using OOP
class GameStats:
    
    def __init__(self):
        """initalizes the health and remaining guesses for the user"""
        self.health = 100
        self.remaining_guesses = 5 
        self.wrong_guesses = []
        self.right_guesses = []
    
    def wrong_guess(self, guess):
        """removes health and guesses for a wrong guess"""
        self.health -= 20
        self.remaining_guesses = self.health // 20  
        self.wrong_guesses += guess
    
    def correct_guess(self, guess):
        """gives back 5 percent health for correct guess"""
        if self.health <= 95:
            self.health += 5 
        self.right_guesses += guess
    
    def __repr__(self):
        return "You have guessed these letters correctly: " + str(self.right_guesses) + "\nYou have guessed these letters incorrectly: "  + str(self.wrong_guesses) + "\nYou have " + str(self.health) + "  percent health\nYou have " + str(self.remaining_guesses) + " guesses left"
    
    
    
    