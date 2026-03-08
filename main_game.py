
from welcome import welcome
from game import game
from difficulty import *

def main():
    
    while True:
        print()
        welcome()
        begin = input("Begin? Type any key (n to quit): ")
        if begin.lower() == "n":
            print("Thanks for trying.")
            quit()
        else:
            print("Game started!")
        
        lim = difficulty()
        game(lim, 1, 100)
    
        again = input("Would you like to play again? Type any key (n to quit): ")
        if again.lower() == "n":
            print()
            print("Thanks for playing!\n")
            quit()
        else:
            print()
            print("restarting...")
        
if __name__ == "__main__":
    main()
