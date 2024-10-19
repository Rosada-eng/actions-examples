import os, sys, time  # Violation of isort (imports not in alphabetical order)

def add(a,b): return a+b  # Violation of Black and pyink (one-liner with no spaces around commas and operators)

def unused_function():
    unused_var = 10  # unused variable
    return None

print(add(  2, 3))  # Violation of Black (excessive spaces inside parentheses)