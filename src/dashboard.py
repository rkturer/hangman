from src.color import Color
from src.player import UserProfile

import pandas as pd

NUMERICAL_METRICS = ["num_characters", "right_guesses", "wrong_guesses", "total_guesses"]

class Dashboard(UserProfile, Color):
    """handles everything related to the dashboard"""

    def __init__(self, username):
        """initalizes everything from the UserProfile class to create the dashboard"""
        super().__init__(username)
        Color.__init__(self)
        self.total = len(self.df["game"])

    @property
    def df(self):
        return pd.read_csv(self.player_stats)

    def find_avg_tail(self, metric):
        """takes a metric as parameter and reads the df to find the average of said metric"""
        if self.total < 5:
            return "Not enough data for metric"
        
        elif metric in NUMERICAL_METRICS:
            my_df= self.df[metric].tail(5)
            answer = round(my_df.mean(),3)
            return answer 
        
        else:
            return "Data must be numerical"
        
    def last_5(self):
        """read the csv file and return a list containing the avg guesses, avg right guesses, and avg wrong guesses in that order"""
        last_5_lst = []

        last_5_total = self.find_avg_tail("total_guesses")
        last_5_wrong = self.find_avg_tail("wrong_guesses")
        last_5_right = self.find_avg_tail("right_guesses")
        
        last_5_lst += [last_5_total]
        last_5_lst += [last_5_wrong]
        last_5_lst += [last_5_right]

        return last_5_lst

    def find_diff(self, avg_total, avg_last_5, metric):
        """find the difference between the two """
        if isinstance(avg_total, str) or isinstance(avg_last_5, str):
            return "Not enough data to compare"
        
        diff = avg_last_5 - avg_total
        diff = round(diff, 3)
        if diff > 0:
            if metric != "wrong_guesses":
                return f"{self.good}{diff} higher than average{self.reset}" 
            else:
                return f"{self.bad}{abs(diff)} lower than average{self.reset}"
        elif diff < 0:
            if metric != "wrong_guesses":
                return f"{self.bad}{abs(diff)} lower than average{self.reset}"
            else:
                return f"{self.good}{abs(diff)} lower than average{self.reset}"
        else:
            return f"the same as average"
        
    def win_percentage(self):
        """reads csv files and find the win percentage of user"""
        result_series = self.df["win"]
        wins = 0
        for rnd in range(self.total):
            if result_series.iloc[rnd]:
                wins +=1
        percentage = round((wins/self.total),3)
        return percentage * 100

    def win_percentage_tail(self):
        """reads csv files and find the win percentage of user"""
        if self.total >= 5:
            r_series = self.df["win"].tail(5)
            result_series = r_series
            wins = 0
            for rnd in result_series:
                if rnd:
                    wins +=1
            percentage = round((wins/5),3)
            return percentage * 100
        else:
            return "Not enough data for metric"
    
    def find_round_data(self):
        """find the right, guesses, wrong guesses, and win status of last game""" 
        round_data = []
        round_guesses = self.df["total_guesses"].iloc[-1]
        round_right_guesses = self.df["right_guesses"].iloc[-1]
        round_wrong_guesses = self.df["wrong_guesses"].iloc[-1]

        if self.df["win"].iloc[-1]:
            result = "won"
        else:
            result = "lost"
        
        round_data += [round_guesses]
        round_data += [round_right_guesses]
        round_data += [round_wrong_guesses]
        round_data += [result]

        return round_data
    
    def dash_input(self):
        """handles user input for the menu of dashboard"""
        while True:
            x = input("Please choose your menu option: ").strip()
            if x == '1':
                return 1
            elif x == '2':
                return 2
            elif x == '3':
                return 3
            elif x == '4':
                return 4
            else:
                print("You must choose from menu above. Please try again")


    def display_dashboard(self):
        """builds and returns the dash board"""
        
        dash_str = ""
        if len(self.username)%2 == 0:
            n = 100
        else: 
            n = 99
        
        dash_str += f"{self.border}{'=' * n}{self.reset}"
        dash_str += "\n\n"
        num_spaces = n - len(self.username)
        half_num_spaces = num_spaces//2
        dash_str += (' ' * half_num_spaces)
        dash_str += f"{self.header}{self.username}{self.reset}"
        dash_str += (" " * half_num_spaces)
        dash_str += "\n\n"
        dash_str += f"{self.border}{'=' * n}{self.reset}"
        dash_str += "\n\n"

        dash_str += f"{self.header}Overall Statistics\n\n{self.reset}"
        dash_str += f"Average win percentage: {round(self.win_percentage(),3)}\n"
        dash_str += f"Average total guesses: {round(self.df['total_guesses'].mean(),3)}\n" 
        dash_str += f"Average wrong guesses: {round(self.df['wrong_guesses'].mean(),3)}\n" 
        dash_str += f"Average right guesses: {round(self.df['right_guesses'].mean(),3)}\n\n" 


        dash_str += f"{self.header}Past Performances: \n\n{self.reset}"

        last_5 = self.last_5()

        round_stats = self.find_round_data()

        dash_str += f"Most Recent Round: You {round_stats[-1]}, had {round_stats[0]} total guesses, {round_stats[1]} right guesses, & {round_stats[2]} wrong guesses.\n\n"

        dash_str += f"{self.header}Past 5 games:\n\n{self.reset}"
        dash_str += f"Average total guesses: {last_5[0]}. This is {self.find_diff(self.df['total_guesses'].mean(), last_5[0], 'total_guesses')}.\n" 
        dash_str += f"Average wrong guesses: {last_5[1]}. This is {self.find_diff(self.df['wrong_guesses'].mean(),last_5[1], 'wrong_guesses')}.\n" 
        dash_str += f"Average right guesses: {last_5[2]}. This is {self.find_diff(self.df['right_guesses'].mean(), last_5[2], 'right_guesses')}.\n"
        dash_str += f"Average win percentage: {self.win_percentage_tail()}. This is {self.find_diff(self.win_percentage(), self.win_percentage_tail(), 'win')}.\n\n"
        
        dash_str += f"{self.border}{'=' * n}{self.reset}"
        dash_str += "\n\n"
        dash_str += f"{self.header}Menu{self.reset}\n"
        dash_str += "|1| Play Game Mode 1 (Random Generated Phrase)\n"
        dash_str += "|2| Play Game Mode 2 (User Generated Phrase)\n"
        dash_str += "|3| Visualize Your Data with a Graph\n"
        dash_str += "|4| Quit\n"
        dash_str += f"{self.border}{'=' * n}{self.reset}\n"

        return dash_str

