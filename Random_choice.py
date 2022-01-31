import random

# Random choice of the player that goes first

def choose_first():
    
    player1 = "Player 1 goes first."
    player2 = "Player 2 goes first."
    
    player1_number = 1
    player2_number = 2
    
    if random.randint(player1_number, player2_number) == player1_number:
        print(player1)
        return player1_number
    else:
        print(player2)
        return player2_number