import random

print ("WELCOME TO ROCK PAPER SCISSORS GAME!!!")

# USER INPUTS
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
user_choice = user_choice.lower()


# You chose: 'rock'
print("You chose:", user_choice)
print(f"You chose: '{user_choice}'")

# VALIDATE USER INPUTS

valid_options = ["rock", "paper", "scissors"]

# breakpoint()
if user_choice not in valid_options:
    print("OOPS INVALID TRY AGAIN")
    exit() # quit()



# COMPUTER CHOICE

#IMPORT RANDOM
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("computer chose:", computer_choice)

# DETERMINE THE WINNER
    # This code is ad
    pted from code in slack by Bonnie during the class 7/12/2022:
    # https://app.slack.com/client/T5XFL5GUE/C5WPFSB52/rimeto_profile/U03K1QDEQFQ
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



# DISPLAY RESULTS
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













