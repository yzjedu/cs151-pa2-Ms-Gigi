# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

1. Initialize Variables:
   1. Set total_sticks to 0. 
   2. Set player1_losses, player2_losses, and computer_losses to 0. 
   3. Set play_again to True.
2. Start Game Loop
   1. While play_again is True:
      1. Set valid_input to False. 
      2. While valid_input is False: 
         1. Prompt user for input: "Enter the number of sticks (10-100):". 
         2. If input is a digit:
            1. Convert the input to an integer (input_count). 
            2. If input_count is between 10 and 100:
               1. Set total_sticks to input_count. 
               2. Set valid_input to True.
            3. Otherwise:
                  Output: "Invalid input. Please enter a number between 10 and 100."
      3. Otherwise:
                  Print: "Invalid input. Please enter a number between 10 and 100."
3. Reset Player Tracking
   1. Set current_player to 0 (Player 1 starts).
   2. Set game_over to False.
4. Turn loop:
   1. While total_sticks is greater than 0 and game_over is False:
      1. Output the current number of sticks. 
      2. If current_player is 2 (Computer's turn):
         1. Generate a random number computer_move (1 to 3).
         2. Output: "Computer takes computer_move sticks."
         3. Subtract computer_move from total_sticks. 
      3. Otherwise (Player's turn):
         1. Set player_num to current_player + 1. 
         2. Set valid_move to False. 
         3. While valid_move is False:
            1. Prompt for input: "Player player_num, enter how many sticks to take (1-3):". 
            2. If input is a digit:
               1. Convert the input to an integer (input_move). 
               2. If input_move is between 1 and 3:
                  1. Subtract input_move from total_sticks.
                  2. Set valid_move to True. 
               3. Otherwise:
                  1. Output: "Invalid move. Please enter 1, 2, or 3."
            3. Otherwise:
               1. Output: "Invalid move. Please enter 1, 2, or 3."
      4. If total_sticks is less than or equal to 0:
         1. Output: "Player player_num loses!"
         2. If current_player is 0:
            1. Increment player1_losses.
         3. Otherwise, if current_player is 1:
            1. Increment player2_losses. 
         4. Otherwise:
            1. Increment computer_losses. 
         5. Set game_over to True.
      5. Set current_player to (current_player + 1) % 3  (to cycle through Player 1, Player 2, and Computer).
5. End of Game:
   1. Output total losses: "Player 1 losses: player1_losses", "Player 2 losses: player2_losses", "Computer losses: computer_losses".
6. Play Again Prompt:
   1. Set valid_response to False. 
   2. While valid_response is False:
      1. Prompt for input: "Do you want to play again? (yes/no):". 
      2. If the response is "yes":
         1. Set play_again to True. 
         2. Set valid_response to True.
      3. Otherwise, if the response is "no":
         1. Set play_again to False. 
         2. Set valid_response to True.
      4. Otherwise:
         1. Output: "Invalid response. Please enter 'yes' or 'no'.".    
