# Initial Design Document

## Algorithm for the Game of Sticks

1. Initialize Variables:
- Set total_sticks to 0 
- Set player1_losses to 0 
- Set player2_losses to 0 
- Set computer_losses to 0 
- Set current_player to 0 (indicating Player 1)
- Set play_again to True (to control whether the game should continue running or not)
2. Game Loop:
- While play_again is True:
    - Get Initial Stick Count:
    - Prompt the user: "Enter the number of sticks (10-100):"
    - Read user input into input_count 
    - Convert input_count to an integer. 
    - Use while loop to validate input_count:
        - If input_count is not an integer or is out of bounds, output "Invalid input. Please enter a number between 10 and 100." and repeat the prompt. 
        - Once valid, set total_sticks to input_count.
    - Reset Player Tracking:
    - Set current_player to 0 (Player 1). 
    - Turn Loop:
    - While total_sticks > 0:
       - Output "Current sticks:", total_sticks. 
       - Check if current_player is 2 (Computer's turn):
          - If true, generate a random number computer_move between 1 and 3. 
          - Output "Computer takes", computer_move, "sticks."
       - Otherwise (if it's Player 1 or Player 2's turn):
          - Prompt the current player: "Player Y, enter how many sticks to take (1-3):" (replace Y with the current player number). 
          - Read user input into input_move. 
          - Convert input_move to an integer. 
          - Use a loop to validate input_move:
             - If input_move is not an integer or is less than 1 or greater than 3, output "Invalid move. Please enter 1, 2, or 3." and repeat the prompt until a valid move is entered.
       - Subtract input_move (or computer_move if it's the computer's turn) from total_sticks.
       - Check if total_sticks == 0:
          - If true, print "Player Y loses!" (replace Y with the current player number). 
          - Increment the respective loss counter:
            - If current_player is 0, increment player1_losses. 
            - If current_player is 1, increment player2_losses. 
            - If current_player is 2, increment computer_losses.
      - Update current_player:
      - Set current_player to (current_player + 1) % 3 (to cycle through Player 1, Player 2, and Computer).
3. End of Game:
- Print "Player 1 losses:", player1_losses. 
- Print "Player 2 losses:", player2_losses. 
- Print "Computer losses:", computer_losses. 
- Ask if players want to play again:
  - Read user input into response. 
  - Check if response equals "yes":
  - If true, set play_again to True. 
  - Otherwise, set play_again to False.
