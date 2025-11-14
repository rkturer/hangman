# **Hangman Terminal Game**

A simplified version of the classic hangman game with two game modes. In the random gamemode you will guess a phrase randomly selected from the data set. In the user input game mode the user to inputs a secret message in the terminal for you to guess. The player can guess letters or the full secret message. Every incorrect letter guess reduces adds a body part to the ascii art hangman. If you try a full guess and are incorrect you lose! If run out of guesses you lose. Good Luck!

## **Description**

A modularized python program with a terminal user interface. The gamestats.py file uses a object oriented programming to store total guesses, number of remaining guesses, a list of the correct guesses and incorrect guesses. The info.py file handles everything related to the phrase inputted by the user or chosen randomly from a hangman_phrases.txt file. Objects of the Phrase class have the these attributes phrase, hidden_phrase, number of characters in phrase and a few others. Methods of the class allow the interface to change the hidden phrase to reveal the correct guesses as well as track the incorrect guesses and remaining guesses. The user.py file handles all of the user input and calls the functions and methods from the other py files to run the game smoothly. The ascii.py file stores the file paths to the ascii art and turns the ascii art into a list with each element being a line. All of the ascii art is in text file in the ascii_art folder. To run the program download all of the py files in the repository and run terminal for the user.py file.

## **About the Creator**

- Rachel Turer - Computer Science and Statistics Major at Boston University
- Email: [rkturer@gmail.com](mailto:rkturer@gmail.com)
- LinkedIn: [Want to Connect?](https://www.linkedin.com/in/rkturer)
