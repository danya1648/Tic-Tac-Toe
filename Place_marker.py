# Applying the selected position to the game board

def place_marker(game_board, marker, position):
    
    game_board[position] = marker
    
    return game_board