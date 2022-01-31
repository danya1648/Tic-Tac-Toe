# This function checks if the game board is full

def full_board_check(game_board):
    
    if " " not in game_board:
        print("The board is full now!")
        return True
    else:
        return False