import os
from src.player import UserProfile
class Login:
    """handles login process for user and the initialization of the user profile object"""

    def __init__(self):
        """initalizes the file path to the file that stores the usernames and passwords """
        self.log = os.path.join("data", "player_login.txt")

    
    def create_account(self):
        """adds a username followed by a password to the player_login.txt file"""
        while True:
            username = input("Enter your username: ")
            if self.verify_user(username):
                print("This username is already taken. Please try again!")
            else:
                while True:
                    password1 = input("Enter password: ")
                    password2 = input("Enter password again: ")
                    if password1 != password2:
                        print("Passwords do not match. Please try again!")
                
                    else:
                        encrypted_password = self.encrypt_password(password1)
                        with open(self.log, "a") as f:
                            f.write(f"{username},{encrypted_password}\n")
                        break

                checker = self.verify_user(username)
                if checker:
                    print("Your account has been created successfully. You will be redirected to login shortly.")
                    user = self.login()
                    return user
                else:
                    print("An error has occured in creating your account. Please try again!")
                
    
    def start_sequence1(self):
        """displays output menu to terminal and innitalizes the userprofile object"""
        print("Welcome to terminal hangman!\n1) Login to your account\n2) Create an account\n3) Play as a guest\n4) Delete your existing account")
        while True:
            choice = input("Pick one of the options above: ").lower().strip()
            if choice == "1":
                return self.login()
            elif choice == "2":
                return self.create_account()
            elif choice == "3":
                return UserProfile("guest")
            elif choice == "4":
                confirmation = input("Are you sure you want to delete your account. Once you do so it cannot be retrieved: (y/n) ")
                if confirmation == "y":
                    username = input("Proceeding to delete your account. Please enter your username: ")
                    self.remove_user(username)
                    if self.verify_user(username):
                        print("An error occured will attempting to delete your account. Please try again.")
                    else:
                        print("Your account has been deleted successfully")
                else:
                    pass
            else:
                print("You must choose one of the options listed in the menu above. Please try again!")
    
    def login(self):
        
        user_count = 0
        pswd_count = 0
        while True:
            if user_count > 2:
                print("\nThe account you are looking for does not exist.\nPlease create an account.\n")
                self.start_sequence1()
            else:
                pass
            username = input("Please enter your username: ")
            user_count +=1 
            if self.verify_user(username):
                while True:
                    if pswd_count > 2:
                        print("You have incorrectly guessed your password atleast 3 times")
                        reset_pswd = input("Would you like to reset your password: (y/n)")
                        if reset_pswd == "y":
                            self.reset_password(username)
                            break
                        else:
                            pass
                    password = input("Please enter your password: ")
                    encrypted_password = self.encrypt_password(password).strip()
                    components = self.lines_to_components(self.file_to_lines())
                    for line in components:
                        if line[-1].strip() == encrypted_password:
                            print(f"Login successful. Welcome, {line[0]}")
                            user = UserProfile(username)
                            return user
                    print("Password is incorrect. Please try again.")
                    pswd_count +=1
            else:
                print("Username not found. Please try again.")   

    def encrypt_password(self, password):
        """takes an arbitrary string s and a non-negative int n between 0 and 25 and retruns a new string in which the letters of s have been rotated n positions"""
        if password == "": #base case
            return ""
        else:
            rest = self.encrypt_password(password[1:]) #recursively calls smaller sub problem
            new_char = self.rotate(password[0])
            return new_char + rest

    
    def rotate(self, c):
        """takes a character c and a non-negative int n as an input and returns a character in the alphabet rotated n units if c is a letter """
        # check to ensure that c is a single character
        assert(type(c) == str and len(c) == 1)
        # Put the rest of your code for this function below.
        if 'a' <= c <= 'z': #checks lowercase
            char = ord(c) + 5 #rotates by end
            if char > ord('z'): #checks if need wrap around
                char = char - 26  #wraps around
        elif 'A' <= c <= "Z": #chekcs uppercase 
            char = ord(c) + 5 #rotates by n 
            if char > ord('Z'): #checks if we need wrap around
                char = char - 26
        else: #c is not in the alphatbet 
            char = ord(c)
        return chr(char)
    
    def file_to_lines(self):
        """takes self as input and returns a list with element corresponding to line in file"""
        lines = []
        with open(self.log, "r") as file:
            for line in file:
                line = line[:-1]
                lines += [line]
        return lines
    
    
    def reset_password(self,username):
        """changes the password in the player_login.txt file"""
        if self.verify_user(username):
            components = self.lines_to_components(self.file_to_lines())
            for profile in components:
                if profile[0] == username:
                    while True:
                        password1 = input("Enter password: ")
                        password2 = input("Enter password again: ")
                        if password1 != password2:
                            print("Passwords do not match. Please try again!")
                        else:
                            encrypted_password = self.encrypt_password(password1)
                            profile[-1] = encrypted_password
                            break
            self.edit_file_with_components(components)
                
    def edit_file_with_components(self, components):
        """edits the play_login.txt file and rewrites with the from the parameter components"""
        with open(self.log, "w") as file:
            for pair in components:
                file.writelines(f"{pair[0]},{pair[1]}\n")

            

    def lines_to_components(self, lines):
        """takes the lines of the text file and changes so they are seperated by fields"""
        components = []
        for line in lines:
            components += [line.split(",")]
        return components

    def remove_user(self, username):
        """removes a username and password fro mteh player_login.txt file"""
        components = self.lines_to_components(self.file_to_lines())
        updated_components = []
        for user in components:
            if username != user[0]:
                updated_components += [user]
        print(updated_components)
        self.edit_file_with_components(updated_components)

    def verify_user(self, username):
        """takes username as a parameter and returns true if the username is registered or false"""
        lines = self.file_to_lines()
        components = self.lines_to_components(lines)
        for fields in components:
            if username == fields[0]:
                return True
        return False

    def __repr__(self):
        """prints all of the usernames in the database"""
        with open(self.log, "r") as file:
            usernames = []
            for line in file:
                line[:-1]
                components = line.split(",")
                usernames += [components[0]]
            return str(usernames)
