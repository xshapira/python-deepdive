# helpers

from .calculator import Calc


# I don't consider the following good style:
# It works, but it might be unexpected for most users.
# They might not even think that the __init__ file
# would contain functional code, so they might be left wondering
# where say_hello and factorial actually came from!

def say_hello(name):
    return f'Hello {name}'


def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
