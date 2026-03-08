
def difficulty_check(choice):
    
    match choice:
        case "Easy":
            lim = 15
        case "Medium":
            lim = 10
        case "Hard":
            lim = 7
        case "Impossible":
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
            print(f"Chosen difficulty: {choice}")
            print(f"You have {lim} tries to guess the number!")
            return lim
        
difficulty()