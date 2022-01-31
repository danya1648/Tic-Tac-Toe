# Displayed information (a board of Tic Tac Toe)

def display_board(game_board):
    print("Here is the current board:")
    print("\n")
    print(game_board[7] + "|" + game_board[8] + "|" + game_board[9])
    print(game_board[4] + "|" + game_board[5] + "|" + game_board[6])
    print(game_board[1] + "|" + game_board[2] + "|" + game_board[3])