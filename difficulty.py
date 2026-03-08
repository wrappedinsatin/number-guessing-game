
def difficulty_check(choice):
    
    match choice:
        case "Easy" | "1":
            lim = 15
        case "Medium" | "2":
            lim = 10
        case "Hard" | "3":
            lim = 7
        case "Impossible" | "4":
            lim = 3
        case _:
            lim = -1
            
    return lim

def difficulty():
    print("Your difficulty options are as follows: ")
    
    lim_lists = ['Easy', 'Medium', 'Hard', 'Impossible']
    
    for i in enumerate(lim_lists, start=1):
        print(i)
    choice = input("Select your difficulty: ").capitalize()
    
    while True:
        
        lim = difficulty_check(choice)
        if lim == -1:
            print(f"Invalid input: {choice} is invalid.")
            choice = input("Select your difficulty: ").capitalize()
        elif lim in [3, 7, 10, 15]:
            print()
            
            if lim == 15:
                print("Chosen difficulty: Easy")
                
            if lim == 10:
                print("Chosen difficulty: Medium")
                
            if lim == 7:
                print("Chosen difficulty: Hard")
                
            if lim == 3:
                print("Chosen difficulty: Impossible")
                
            print(f"You have {lim} tries to guess the number!")
            return lim