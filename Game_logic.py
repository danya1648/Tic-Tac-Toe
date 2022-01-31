# Modules

import Display_information
import Start_of_game
import Place_marker
import Win_check
import Random_choice
import Full_board_check
import Player_choice
import Replay

# Game logic

print("Welcome to the Tic Tac Toe game!")


while True:
    # Set the game up here
    
    # Displayed information (a board of Tic Tac Toe)
    game_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_on = True
    Display_information.display_board(game_board)
    # Start of the game. The choice of X or O
    player1_marker, player2_marker = Start_of_game.player_input()
    # Random choice of the player that goes first
    print("Now let us randomly choose which player goes first.")
    choice = Random_choice.choose_first()
    while game_on:
        if choice == 1:
         # Player1 turn
            position = Player_choice.player_choice(game_board)
            game_board = Place_marker.place_marker(game_board, player1_marker, position)
            Display_information.display_board(game_board)
            check_of_board = Full_board_check.full_board_check(game_board)
            check_of_winner = Win_check.win_check(game_board, player1_marker)
            if check_of_board == True or check_of_winner == True:
                game_on = False
            choice = 2
        else:
        # Player2 turn
            position = Player_choice.player_choice(game_board)
            game_board = Place_marker.place_marker(game_board, player2_marker, position)
            Display_information.display_board(game_board)
            check_of_board = Full_board_check.full_board_check(game_board)
            check_of_winner = Win_check.win_check(game_board, player2_marker)
            if check_of_board == True or check_of_winner == True:
                game_on = False
            choice = 1
        
    if Replay.replay():
        game_on = True
    else:
        break