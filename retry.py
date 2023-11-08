from functools import wraps
import random
from typing import Callable


def retry(f: Callable):
    @wraps(f)
    def wrapper(*args, **kwds):
        """Run f until it return a value that is not None and return the result."""
        f_return_value = None
        while f_return_value is None:
            f_return_value = f(*args, **kwds)
        return f_return_value
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