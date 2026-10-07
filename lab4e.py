# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

def compute(num1=int, num2=int, opperation="+"):
    '''
    This function will compute 2 given numbers and a given opperation
    @param 2 integers and an opperation
    @return The integers computed by the opperation
    '''
    if opperation == "*":
        result = num1 * num2
    elif opperation == "/":
        result = num1 / num2
    elif opperation == "+":
        result = num1 + num2
    elif opperation == "-":
        result = num1 - num2
    else:
        result == num1 + num2
    return print(result)

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    z = input("Enter an opperation (+ addtion, - subtraction, * multiplication, or / division): ")
    compute(num2=x, num1=y, opperation=z)
    compute(opperation=z, num2=y, num1=x)


if __name__ == "__main__":
    main()