import os
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

NUMERICAL_METRICS = ["num_characters", "right_guesses", "wrong_guesses", "total_guesses"]
CATEGORICAL_METRICS = ["game", "win", "is_random", "full_guess"]
CATEGORICAL_LABELS = {
                        "win" : ["wins", "losses"],
                        "game" : ["hangman", "other"],
                        "is_random" : ["random", "user_input"],
                        "full_guess" : ["used_full_guess", "did_not_use_full_guess"]
                    }

class Graphing:

    def __init__(self):
        
        
        self.graph = self.graph_type()
    

    def graph_type(self):
        """offers a menu of graph and takes user input and returns the type of graph they want"""

        print("Graph Options:\n1) scatter plot\n2) Histogram\n3) Pie Chart")
        while True:
            self.graph = input("Please choose a graph from the menu above.").strip()
            if self.graph == "1":
                return 'scatter'
            elif self.graph == "2":
                return 'hist'
            elif self.graph == "3":
                return 'pie'
            else:
                print("You must pick an option above.\nFor example, to pick a Pie Chart enter '1'")
    
    
    def collect_numerical_axes(self):
        if self.graph == 'scatter':
            while True:
                x_axis = input("Please enter the metric for the x axis: ")
                if self.is_numerical(x_axis):
                    y_axis = input("Please enter the metric for the y axis: ")
                    if self.is_numerical(y_axis):
                        print("Metrics successfully collected.")
                        return x_axis, y_axis
                    else:
                        print("Your metric must be numerical for a scatterplot. Please try again.")
                        
                else:
                    print("Your metric must be numerical for a scatterplot. Please try again.")
        else:
            print("Given graph was not numerical")

    def collect_numerical_axis(self):
        """takes user input to collect numerical metric for histogram"""
        if self.graph == 'hist':
            while True:
                x_axis = input("Please enter the metric for the x axis: ")
                if self.is_numerical(x_axis):
                    return x_axis
                else:
                    print("Your metric must be numerical for a histogram. Please try again.")
        else:
            print("Invalid graph has been inputted")

    def collect_categorical_metrics(self):
        if self.graph == "pie":
            while True:
                metric = input("What metric would you like to visualize? ")
                if self.is_categorical(metric):
                    print("Metric successfully collected.")
                    return metric
                else:
                    print("Metric must be categorical.")
        else:
            print("Given graph was not categorical")

    def create_scatter_plot(self, x_axis, y_axis, user):
        """takes two numerical categories as parameters and saves a scatter plot of them into a folder for user"""
        df = pd.read_csv(user.player_stats)
        df.plot(kind = "scatter", x = x_axis, y = y_axis)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"{x_axis} vs {y_axis}")
        plot_title_saved = f"{x_axis}_{y_axis}_scatter.png"

        while True:
            regression = input("Would you like a regression line? (y/n) ").lower().strip()
            if regression == "y":
                slope, y_int = np.polyfit(df[x_axis], df[y_axis], 1)
                plt.plot(df[x_axis], df[x_axis]*slope +y_int, label="Regression Line")
                break
            elif regression == "n":
                break
            else:
                print("You must chose yes (y) or no (n) to continue. ")


        if self.duplicate(plot_title_saved, user):
            if not self.overwrite():
                plot_title_saved = self.custom_name(user)
        path = os.path.join(user.username_plots, plot_title_saved)
        plt.savefig(path)
        plt.show()

    
    def create_hist(self, x_axis, user):
        """takes x_axis as parameter and create and saves a histogram"""
        df = pd.read_csv(user.player_stats)
        data = df[x_axis]
        plt.hist(data, edgecolor = "black")
        plt.xlabel(x_axis)
        plt.ylabel("Frequency")
        plt.title(f"{x_axis} histogram")
        plot_title_saved = f"{x_axis}_hist.png"
        
        if self.duplicate(plot_title_saved, user):
            if not self.overwrite():
                plot_title_saved = self.custom_name(user)
        path = os.path.join(user.username_plots, plot_title_saved)
        plt.savefig(path)
        plt.show()
        
    
    def create_pie_chart(self, metric, user):
        """takes a metric as parameter and saves a pie chart of the metric to the player data folder"""
        df = pd.read_csv(user.player_stats)
        metric_counts = df[str(metric)].value_counts()
        plot_title_saved = f"{metric}_pie.png"
        labels = self.make_labels_pie(metric)

        if self.duplicate(plot_title_saved, user):
            if not self.overwrite():
                plot_title_saved = self.custom_name(user)
        
        metric_counts.plot(kind = "pie", labels = labels, autopct='%1.1f%%' )
        path = os.path.join(user.username_plots, plot_title_saved) 
        plt.title(str(metric))
        plt.savefig(path)
        plt.show()
    
    def make_labels_pie(self, metric):
        """takes a metric as parameter and turns appropraite labels for pie chart"""
        for met in CATEGORICAL_LABELS:
            if metric == met:
                return CATEGORICAL_LABELS[met]
        return "Error has occurred"


    def custom_name(self, user):
        """takes no inputs but returns a custom name for the file to be saved as in case of duplicate"""
        while True:    
            name = input("Enter a custom name for the chart to be saved as: ")
            if self.duplicate(name , user):
                print("A chart is already saved under this name. Try a different one. ")
            else:
                return name 

    def overwrite(self):
        """takes user input on if they want to overwrite the current plot return boolean True False"""
        while True:
            overwrite = input("You already have a plot saved with the same metrics. Would you like to overwrite the chart with more current data? (y/n) ").lower().strip()
            if overwrite == "y":
                return True
            elif overwrite == "n":
                return False
            else:
                print("You must pick yes (y) or no (n) to continue")

    def duplicate(self, plot_title, user):
        """takes a plot title and returns true if there is already a plot with the same title in the folder"""
        current_graph_titles = os.listdir(user.username_plots)
        for title in current_graph_titles:
            if title == plot_title:
                return True
        return False  
    
    def is_numerical(self, input_metric):
        """takes a metric from a user and returns true if the metric is tracked in the CSV file otherwise returns false"""
        
        for ele in NUMERICAL_METRICS:
            if ele == input_metric:
                return True
        return False 
    
    def is_categorical(self, metric):
        """takes a metric from user and returns True if it is categorical data otherwise returns False"""

        for ele in CATEGORICAL_METRICS:
            if metric == ele:
                return True
        return False

    def plotter(self, user):
        
        if self.graph == 'scatter':
            x, y = self.collect_numerical_axes()
            self.create_scatter_plot(x, y, user)
        elif self.graph == 'hist':
            x = self.collect_numerical_axis()
            self.create_hist(x, user)
        elif self.graph == 'pie':
            metric = self.collect_categorical_metrics()
            self.create_pie_chart(metric, user)
        else:
            print("Invalid graph has been entered")

    def display_tracked_fields(self):
        """takes no parameters but prints the metrics tracked in the csv files"""
        print("The CSV files tracks the following metrics:\nBooleans: game, win, is_random, full_guess\nNumerical: total_guesses, right_guesses, wrong_guesses, num_characters")



