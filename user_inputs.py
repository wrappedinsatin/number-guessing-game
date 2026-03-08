from test_number import test_int

def user_input():
    num = input("Please type in an integer between 1 and 100: ")
    test_int(num, 1, 100)
