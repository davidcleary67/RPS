#!/usr/bin/python3

# Rock paper scissors game

# Import random library
import random

# Main function
def main():
    
    # Repeatedly compare user and computer guesses
    
    # Get first user guess
    user = input("Your guess [r]ock, [p]aper, [s]cissors, [e]xit: ")
    
    # Repeat while user guess is not "e for exit"
    while user != "e":
        
        # Get and print computer guess
        comp = random.choice(["r", "p", "s"])
        print(f"Computer's guess: {comp}")
        
        # Determine result
        if user == comp:
            result = "Draw"
        elif (user == "r" and comp == "s") or (user == "p" and comp =="r") or (user == "s" and comp == "p"):
            result = "You Win!"
        else:
            result = "You Lose!"
        
        # Print result
        print(result)
    
        # Get new user guess
        user = input("Your guess [r]ock, [p]aper, [s]cissors, [e]xit: ")

# Call main function
if __name__ == '__main__':
    main()