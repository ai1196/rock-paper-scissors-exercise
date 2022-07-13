# this is the "game.py" file...

import random

print("Rock, Paper, Scissors, Shoot!")

# USER INPUTS

user_choice = input("Please make a selection ('rock', 'paper', 'scissors'): ")

# You chose: 'rock'
print(f"You chose: '{user_choice}' ")


# VALIDATE USER UNPUTS


# COMPUTER CHOICE
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)


# DETERMINE THE WINNER


# DISPLAY THE RESULTS 


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