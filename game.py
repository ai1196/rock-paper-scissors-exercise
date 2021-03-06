# this is the "game.py" file...

import random

print("Rock, Paper, Scissors, Shoot!")

print("Welcome 'Player One' to my Rock, Paper, Scissors, Shoot Game!")

# USER INPUTS
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'): ")

# STANDARIZING THE USER INPUT
user_choice = user_choice.lower()

# You chose: 'rock'
print(f"You chose: '{user_choice}' ")

# VALIDATE USER UNPUTS
valid_options = ["rock", "paper", "scissors"]

# IF NOT VALID OPTIONS ENTERED
if user_choice not in valid_options:
    print ("OOPS INVALID, TRY AGAIN")
    exit()

# COMPUTER CHOICE
computer_choice = random.choice(valid_options)
print(f"Computer chose: '{computer_choice}' ")

# DETERMINE THE WINNER + DISPLAY THE RESULTS 
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

# FAREWELL MESSAGE
print("Thanks for playing. Please play again!")


# 
# -------------------
# Welcome 'Player One' to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!