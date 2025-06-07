"""
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
"""

"""
import time

def count_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start:.2f} sec.")
        return result
    return wrapper

@count_execution_time
def slow_function():
    time.sleep(2)
    print("Function complete!")

slow_function()
"""

import random

def attempt(max_count=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_count:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    print(f"Error: {e}! Attempt {retries}/{max_count}")
            print("Failed after maximum retries")
        return wrapper
    return decorator

@attempt(5)
def unstable():
    if random.choice([True, False]):
        raise ValueError("Random Failure!")
    print ("Success!")

unstable()
