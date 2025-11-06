# **Hangman Terminal Game**

A simplified version of the classic hangman game. After the user to inputs a secret message in the terminal the program hides it behind "#"s. The user then can guess letters or the full secret message. Every incorrect letter guess reduces health by 20%; every correct letter guess increases health by 5%. If your health reaches zero you lose. Good Luck!

##**Description**

A modularized python program with a terminal user interface. The gamestats.py file uses a object oriented programming to store health, number of remaining guesses, a list of the correct guesses and incorrect guesses. The guesser.py file handles hiding the phrase inputted by the user. As well as checking if the guessed character is within the phrase and updating the hidden phrase to have the guessed letters. The user.py file handles all of the user input and calls the functions and methods from the other py files to run the game smoothly. To run the program download all of the py files in the repository and run terminal for the user.py file.

##**About the Creator

- Rachel Turer - Computer Science and Statistics Major at Boston University
- Email: [rkturer@gmail.com](mailto:rkturer@gmail.com)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/rkturer)
