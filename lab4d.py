# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

def compute(num1, num2, opperation="+"):
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
        return "ERROR"
    return print(result)

def main():
    compute(13,45,'*')
    
    compute(13,45,'/')
    compute(13,45,'-')
    compute(13,45,'+')
    compute(13,45)

    x = int(input("Enter a number: "))
    y = int(input("Enter a second number: "))
    z = input("Enter an opperation (+ addtion, - subtraction, * multiplication, or / division): ")
    compute(x, y, z)


if __name__ == "__main__":
    main()