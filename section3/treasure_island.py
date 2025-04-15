print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
side = input('You are at a crossroad, where do you want to go? Type "left" or "right": ').lower()


if(side == "left"):
    print("\n")
    action = input("You've come to a lake, and there is an island in the middle of the lake.\n" 
               "Type 'wait' to wait for a boat. \n"
               "Type 'swim' to swim across: ").lower()
    
    if(action == "swim"):
        print("\n")
        door = input("You arrive at the island unharmed. \n"        
             "There is a house with 3 doors. \n"
             "One red, one yellow and one blue \n"
             "Wich colour do you choose? ").lower()
        
        if(door == "red"):
            print("\n")
            print("The room you entered is on fire, you were burned to death. Game over!")
        elif(door == "yellow"):
            print("\n")
            print("You found a chest full of treasures. You win!")
        elif(door == "blue"):
            print("\n")
            print("The room you entered is full of beasts. Game over!")
        else:
            print("\n")
            print("You entered in a room where a mafia meeting was occurring. They shot you to death. Game over!")

    else:
        print("\n")
        "As you were swimming, you were attacked by a shark. Game over!"
    
else:
    print("You fell into a hole. Game over!")