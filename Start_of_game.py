# Start of the game. The choice of X or O

def player_input():
    
    game_start = " "
    
    while game_start not in ["X", "O"]:
        game_start = input("Player 1! Do you want to play for X or O? ")
        print("\n"*100)
        
        if game_start not in ["X", "O"]:
            print("Please select X or O.")
    
    player1 = game_start
    
    
    if player1 == "X":
        player2 = "O"
        print("Player 1 has selected X to play the game. Then player 2 will play for O.")
    else:
        player2 = "X"
        print("Player 1 has selected O to play the game. Then player 2 will play for X.")
        
    return (player1, player2)