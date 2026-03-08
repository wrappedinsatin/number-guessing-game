
def test_int(lower_bound, upper_bound):
    
    while True:
    
        print("Make your guess!")
        num = input(">")
    
        try:
            num = int(num)
            print()
        
            if not lower_bound <= num <= upper_bound:
                print(f"Out of range!: {num} is not within the specified range.")
                print(f"type in a number between {lower_bound} and {upper_bound}.\n")
            else:
                return num
        
        except ValueError:
            print(f"{num} is not an integer!")
            print("Type in an integer.\n")