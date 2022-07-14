# Rock Paper Scissor Exercise
The following instructions will help you set up a python application that allows you to play rock, paper, scissors with a computer. Try your luck!

## Setup
On GitHub, create a new project repository and name it something like "rock-paper-scissors-exercise." When prompted, be sure to add a "README.md" file and a Python ".gitignore" file. You can optionally add a license. 

Use GitHub Desktop software or the command-line to download or "clone" the remote repository onto your computer. This will be referred to as the "local repository."

Use your command-line applications to navigate into the local repository (using one or more `cd` commands):
```sh
cd ~/Desktop/rock-paper-scissors-exercise
```

Using your text editor or the command-line application, create a new file in that repo called "game.py," and place the following contents inside that new file.
```sh
print("Rock, Paper, Scissors, Shoot!")
```

## Environment Setup
Create and activate a new virtual environment:
```
conda create -n my-game-env python=3.8
```

Activate the virtual environment:
```
conda activate my-game-env
```

If necessary, install package dependencies within the virtual environment:
```
pip install -r requirements.txt
```

When you see the "Rock, Paper, Scissors, Shoot!" message then you're good to go onto the requirements for development. 

## Requirements
Once you have completed the setup steps above, you can continue with the rest of the exercise implementation. 

### Processing Inputs
The application should prompt the user to make a selection from a list of valid options (i.e. "rock", "paper", "scissors") via command-line interface (CLI). It should store the user's selection in a variable for later reference (i.e. "user_selection")

### Validating User Inputs
The applications should compare the user's selection against a list of valid options (i.e. "rock", "paper", "scissors") to confirm that the user has selection a valid option needed to play the game successfully. 

It should be able to handle various capitalizations of the valid options (e.g., "ROCK", "Rock", or "rock").

If the selection is invalid, the program should display a friendly message and prevent further program execution. The program should not try to further process an invalid input as it can lead to runtime errors.

### Simulating Computer Selection
The applications should select one of the options (i.e. "rock", "paper", "scissors") at random, and assign that as the computer player's choice. 

### Determining the Winner
The application should compare the user's choice with the computer player's choice to determine a winner. The following logic should govern that determination:
1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Rock vs Rock, Paper vs Paper, Scissors vs Scissors each results in a "tie"

### Displaying the Results
Once a winner is determined, the application should display the results to the user. Outputs should include at least one of the following:
+ A Friendly Welcome message including the player's name (by default, user "Player One")
+ The user's selection option
+ The computer's selected option
+ Whether the user or th computer was the winner 
+ A friendly farewell message

Here's an example of a desired output after one round of game-play:
```
----------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
----------------
Please choose either 'rock', 'paper', or 'scissors': rock
You chose: 'rock'
The computer chose: 'paper'
----------------
Oh, the computer won. Its ok.
----------------
Thanks for playing. Please play again!
```

## Game play
Play Rock, Paper, Scissors with the computer:
```
python game.py
```



