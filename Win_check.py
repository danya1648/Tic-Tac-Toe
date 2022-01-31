# Win combinations: 1-2-3, 4-5-6, 7-8-9, 1-5-9, 3-5-7, 1-4-7, 2-5-8, 3-6-9.

def win_check(game_board, mark):
    
    if game_board[1] == game_board[2] == game_board[3] == mark:
        print("We have a winner here. Congratulations!")
        return True
        
    elif game_board[4] == game_board[5] == game_board[6] == mark:
        print("We have a winner here. Congratulations!")
        return True
    
    elif game_board[7] == game_board[8] == game_board[9] == mark:
        print("We have a winner here. Congratulations!")
        return True
    
    elif game_board[1] == game_board[5] == game_board[9] == mark:
        print("We have a winner here. Congratulations!")
        return True
        
    elif game_board[3] == game_board[5] == game_board[7] == mark:
        print("We have a winner here. Congratulations!")
        return True
    
    elif game_board[1] == game_board[4] == game_board[7] == mark:
        print("We have a winner here. Congratulations!")
        return True
        
    elif game_board[2] == game_board[5] == game_board[8] == mark:
        print("We have a winner here. Congratulations!")
        return True
        
    elif game_board[3] == game_board[6] == game_board[9] == mark:
        print("We have a winner here. Congratulations!")
        return True
        
    else:
        print("Keep playing the game, guys!")
        return False