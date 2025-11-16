import os
class UserProfile:
    """handles a players profile"""

    def __init__(self, username):
        """initalizes the userprofile object with username and the file path to the user text file"""
        self.username = username

        self.folder = "player_data"
        os.makedirs(self.folder, exist_ok=True)

        self.player_stats = os.path.join(self.folder, f"{self.username}.csv")

        self.username_plots = os.path.join(self.folder, f"{self.username}_plots")

        os.makedirs(self.username_plots , exist_ok=True)

        if not os.path.exists(self.player_stats):
            with open(self.player_stats, "w") as file:
                file.write("game,win,full_guess,total_guesses,right_guesses,wrong_guesses,num_characters,is_random\n")


    def add_game_to_file(self, stats, info):
        """opens the user textfile and updates it with the most recent game stats"""
        with open(self.player_stats, "a") as file:
            file.write(f"{stats.game},{stats.win},{stats.full_guess},{stats.total_guesses},{len(stats.right_guesses)},{len(stats.wrong_guesses)},{info.num_chars},{info.is_random}\n")

    def __repr__(self):
        return f"The user logged in is {self.username}"



