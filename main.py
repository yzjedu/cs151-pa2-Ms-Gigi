# Programmer Name: Oreoluwa Adebusoye
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/23/2024
# Program Name: Stick Game
# What program does (purpose): This is a simple interactive game where players take turns removing a specified number of sticks (1, 2, or 3) from a pile.
#                             The objective is to avoid being the player who takes the last stick.

# Introduction to the Game
print("Welcome to the Stick Game!")
print("The goal is to avoid being the player who takes the last stick.")
print("Players can take 1, 2, or 3 sticks on their turn.")
print("The game starts with a number of sticks between 10 and 100.")
print("Let's begin!")

# Allows the program to generate random numbers
import random

# Initialize Variables
total_sticks = 0
player1_losses = 0
player2_losses = 0
computer_losses = 0
play_again = True   # Control variable to determine if the game should continue.

while play_again:
    # Get Initial Stick Count
    valid_input = False
    while not valid_input:
        input_count = input("Enter the number of sticks (10-100): ")
        if input_count.isdigit():
            input_count = int(input_count)
            if 10 <= input_count <= 100:
                total_sticks = input_count
                valid_input = True
            else:
                print("Invalid input. Please enter a number between 10 and 100.")
        else:
            print("Invalid input. Please enter a number between 10 and 100.")

    # Reset Player Tracking
    current_player = 0  # Player 1 starts
    game_over = False

    # Turn Loop
    while total_sticks > 0 and not game_over:
        print(f"\nCurrent sticks: {total_sticks}")

        if current_player == 2:  # Computer's turn
            computer_move = random.randint(1, 3)
            print(f"Computer takes {computer_move} sticks.")
            total_sticks -= computer_move
        else:  # Player 1 or Player 2's turn
            player_num = current_player + 1
            valid_move = False
            while not valid_move:
                input_move = input(f"Player {player_num}, enter how many sticks to take (1-3): ")
                if input_move.isdigit():
                    input_move = int(input_move)
                    if 1 <= input_move <= 3:
                        total_sticks -= input_move
                        valid_move = True
                    else:
                        print("Invalid move. Please enter 1, 2, or 3.")
                else:
                    print("Invalid move. Please enter 1, 2, or 3.")

        # Check for loss
        if total_sticks <= 0:
            print(f"Player {player_num} loses!")
            if current_player == 0:
                player1_losses += 1
            elif current_player == 1:
                player2_losses += 1
            else:
                computer_losses += 1
            game_over = True

        # Update current player
        current_player = (current_player + 1) % 3  # Cycle through 0, 1, 2

    # End of Game
    print(f"\nGame Over! Here are the results:")
    print(f"Player 1 losses: {player1_losses}")
    print(f"Player 2 losses: {player2_losses}")
    print(f"Computer losses: {computer_losses}")

    # Ask if players want to play again
    valid_response = False
    while not valid_response:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response == "yes":
            play_again = True
            valid_response = True
        elif response == "no":
            play_again = False
            valid_response = True
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
print("Thank you for playing the Stick Game! Goodbye!")