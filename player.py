
class UserProfile:
    """handles a players profile"""

    def __init__(self, username):
        self.username = username
        self.player_stats = f"{self.username}.txt"

    def add_game_to_file(self, stats, info):
        with open(self.player_stats, "a") as file:
            file.write(f"{stats.game},{stats.win},{stats.full_guess},{stats.total_guesses},{len(stats.right_guesses)},{len(stats.wrong_guesses)},{info.num_chars},{info.is_random}\n")

    def __repr__(self):
        return f"The user logged in is {self.username}"
