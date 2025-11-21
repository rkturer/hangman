# **User.txt ReadMe**

After each round of hangman, if the user is logged in, a text file {username}.txt will update with the results of the most recent game. The file is in CSV format. The saved statistics include: 

game(str),win(boolean),full_guess(boolean),total_guesses(int),right_guesses(int),wrong_guesses(int),num_characters(int),random(boolean)

## **IMPORTANT NOTES**

The users data only gets updated if they are logged in. If the user elects to play as a guest, their data gets stored the a guest file. 
