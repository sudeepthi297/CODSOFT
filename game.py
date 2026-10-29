
import random

# Available choices in the game
choices = ["rock", "paper", "scissors"]


# Function to decide the winner
def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a Tie!"

    elif user_choice == "rock" and computer_choice == "scissors":
        return "You Win!"

    elif user_choice == "scissors" and computer_choice == "paper":
        return "You Win!"

    elif user_choice == "paper" and computer_choice == "rock":
        return "You Win!"

    else:
        return "You Lose!"


# Main game
print("================================")
print("   ROCK PAPER SCISSORS GAME")
print("================================")
print("Type rock, paper, or scissors.")
print("Type quit to exit the game.")

while True:

    # Get the user's choice
    user_choice = input("\nEnter your choice: ").lower().strip()

    # Exit the game
    if user_choice == "quit":
        print("Thanks for playing!")
        break

    # Check whether the input is valid
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Generate the computer's choice
    computer_choice = random.choice(choices)

    # Display both choices
    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    # Find and display the winner
    result = get_winner(user_choice, computer_choice)
    print("Result:", result)
