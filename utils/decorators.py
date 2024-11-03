from typing import List
from functools import wraps


def check_roles(roles: List[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)

            return func(*args, **kwargs)
        return wrapper
    return decorator
