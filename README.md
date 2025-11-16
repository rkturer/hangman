# **Hangman Terminal Game**

[screenshot of hangman setup](/assets/hangman.png)

A version of the classic hangman game with two game modes. In the Random Game Mode you will guess a phrase randomly selected from the data set. In the user input game mode the user inputs a secret message in the terminal for the player to guess. The player can guess letters or the full secret message. Every incorrect letter guess adds a body part to the ascii art hangman. If you try a full guess and are incorrect you lose! If you run out of guesses, you lose. Good Luck!

## **Description**

A terminal hangman game that asks the user to log in, create an account, or play as a guest. If logged in stats are tracked for each user. To learn more about the stats read [CSV_README.md](user_text_files_README.md). Users get to enjoy two Game Modes and ASCII art to display the game. This project demonstrates OOP, file handling, and UI. 

Below is a screenshot of the user authentication: 

[user authentication screenshot](/assets/user_auth.png)

## **Features**

- User Data Analytics & Plot Generations (CSV-based statistics and visualization)
- User Accounts (Login, Create, Delete, Update Password)
- Password Encryption (Simple Rotation Cipher)
- User Profile Statistics Saved To CSV 
- 2 Game Modes (Random Phrase & User Input Phrase)
- ASCII Art for Terminal Display 
- Tracking of correct guesses, incorrect guesses, remaining guesses, and dynamically filled in hidden phrase

## **User Statistics and Analytics**

After each round of hangman the game stats explained in [CSV_README.md](CSV_README.md) are added to the user's personalized CSV file. The user also enjoys a personal folder storing all of their analytic visualizations (histograms, pie charts, scatter plots). The user also enjoys an interactive UI where they can create custom charts by following on screen prompts. 

Below is an example output of the program:

[Analytics Screenshot](/assets/analytics.png)

## **Folder Structure**

```
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
        /user files and plots
    /assets
        /analytics.png
        /hangman.png
        /user_auth.png
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
```

## **Installation**

This project has matplotlib, pandas, and numpy as dependencies. Install using the line below: 

`pip install -r requirements.txt`

## **How To Play**

1. Run `run_game.py`
2. Follow menu prompts 
3. Choose your Game Mode
4. Guess letters and attempt to solve the phrase 
5. Play until you win or lose! 

## **Classes and Modules**

- Login - Handles user authentication and password management 
- Graphing - Handles UI, reading CSV files, and generation of plots 
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
- More Data Analytics for CSV files 

## **About the Creator**

- Rachel Turer - Computer Science and Statistics Major at Boston University
- Email: [rkturer@gmail.com](mailto:rkturer@gmail.com)
- LinkedIn: [Want to Connect?](https://www.linkedin.com/in/rkturer)
