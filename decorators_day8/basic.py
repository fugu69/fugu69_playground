def decorator(original_func):   # any name, needs original function as an argument
    def wrapper():              # necessary part, name is for convinience the same
        print("Start Game")
        original_func()
        print("End Game")
    return wrapper
        

@decorator
def middle_game():
    print("Middle Game")

middle_game()
