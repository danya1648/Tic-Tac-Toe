# The player chooses a position from 1 to 9

def player_choice(game_board):
    
    position = "Not a digit"
    acceptable_range = range(1,10)
    within_range = False
    
    while position.isdigit() == False or within_range == False:
        position = input("Please choose a 'numpad' position from 1 to 9: ")
        print("\n"*100)
        
        if position.isdigit() == False:
            print("Please use numeric values only: 1,2,3,4,5,6,7,8,9.")
            
        if position.isdigit() == True:
            if int(position) in acceptable_range:
                if game_board[int(position)] == " ":
                    within_range = True
                else:
                    print("Please do not apply numbers that were previously selected in this game.")
                    within_range = False
            else:
                print("Please select a number within the acceptable range (1-9).")
                within_range = False
                
    return int(position)