# **Hangman Terminal Game**

A version of the classic hangman game with two game modes. In the random gamemode you will guess a phrase randomly selected from the data set. In the user input game mode the user to inputs a secret message in the terminal for the player to guess. The player can guess letters or the full secret message. Every incorrect letter guess reduces adds a body part to the ascii art hangman. If you try a full guess and are incorrect you lose! If run out of guesses, you lose. Good Luck!

## **Description**

A terminal hangman game that asks the user to log in, create an account, or play as a guest. If logged in stats are tracked for each user. To learn more about the stats read [CSV_README.md](user_text_files_README.md). Users get to enjoy two gamemodes and ASCII art to display the game. This project demonstrates OOP, file handling, and UI. 

## **Features**

- User Accounts (Login, Create, Delete, Update Password)
- Password Encryption (Simple Rotation Cipher)
- User Profile Statistics Saved To CSV 
- 2 gamemodes (Random Phrase & User Input Phrase)
- ASCII Art for Terminal Display 
- Tracking of correct guesses, incorrect guesses, remaining guesses, and dynamically filled in hidden phrase

## **Folder Structure**

/hangman
    /ascii_art 
        art_hangman_0.txt 
        art_hangman_1.txt 
        art_hangman_2.txt 
        art_hangman_3.txt 
        art_hangman_4.txt 
        art_hangman_5.txt 
        art_hangman_6.txt 
        art_hangman_win.txt
    /data
        hangman_phrases.txt
        player_login.txt
    /player_data
    /src 
        ascii.py 
        gamestats.py
        info.py
        login.py
        player.py
        users.py
    .gitignore
    README.md
    requirements.txt
    run_game.py
    user_text_files_README.md

## **Installation**

This project has no dependencies 

## **How To Play**

1. Run `run_game.py`
2. Follow menu prompts 
3. Choose your gamemode
4. Guess letters and attempt to solve the phrase 
5. Play until you win or lose! 

## **Classes and Modules**

- Login - Handles user authentication and password management 
- Ascii - Handles updating the ASCII art to match phase of the game
- UserProfile - Handles creating CSV files to store user data
- GameStats - Handles storing game statistics to be placed into the CSV files
- Phrase - Handles everything related to the secret phrase of the game
- run_game.py - Main entry point for game, runs all other files 

## **Notes and Known Issues**

- Project is still in progress. If given unexpected input program may terminate 
- This project is for learning purposes only. Passwords are stored with a simple character rotation and are NOT secure
- Player data CSV file grows with each run of the program

## **Future Improvements**

- Error Handling for UI 
- Data Analytics for CSV files 

## **About the Creator**

- Rachel Turer - Computer Science and Statistics Major at Boston University
- Email: [rkturer@gmail.com](mailto:rkturer@gmail.com)
- LinkedIn: [Want to Connect?](https://www.linkedin.com/in/rkturer)
