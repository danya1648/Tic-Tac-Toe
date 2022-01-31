# The players are asked if they want to replay the game

def replay():
    
    choice = "Default value"
    range_of_choices = ["Y", "N"]
    
    while choice not in range_of_choices:
        choice = input("Do you want to replay the game? Y or N. ")
        print("\n"*100)
        
        if choice not in range_of_choices:
            print("Please select either Y or N.")
        
    if choice == "Y":
        return True
    else:
        return False