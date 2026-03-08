
from random import randint
from test_number import test_int

def game(lim, lower_bound, upper_bound):
    
    selected = randint(lower_bound, upper_bound)
    count = 0
    
    while True:
        
        num = test_int(lower_bound, upper_bound)
        count += 1
        
        if num != selected:
            if num < selected:
                print(f"{num} is smaller than the guess!")
                
            if num > selected:
                print(f"{num} is greater than the guess!")
                
        
        if count <= lim and num == selected:
            
            print(f"Correct! The number was {selected}.")
            
            if count == 1:
                print("You guessed the correct number in a single attempt!")
            else:
                print(f"It took you {count} tries!")
            break
                
        if count > lim:
            print()
            print(f"Too many guesses!")
            print(f"The number was {selected}")
            break