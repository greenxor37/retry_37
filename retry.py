from functools import wraps
import random
from typing import Callable


def retry(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwds):
        """Run the function until it return a value that is not None and return the result."""
        func_return_value = None
        while func_return_value is None:
            func_return_value = func(*args, **kwds)
        return func_return_value
    return wrapper


@retry
def return_three():
    number = random.randint(0, 5)
    if number == 3:
        return number      


@retry
def return_divided_three():
    number = random.randint(0, 10)
    if number % 3 == 0:
        return number      


def main():      
    print('return_three():', return_three())
    print('return_divided_three():', return_divided_three())
    
    
if __name__ == "__main__":
    main()