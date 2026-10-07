# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

def sum(num1, num2):
    '''
    This function will add two numbers together.
    @param Two integers
    @return sum
    '''
    total = num1 + num2
    return total

def main():
    x = int(input("Please select a number: "))
    y = int(input("Please select another number: "))
    print(sum(x, y))

if __name__ == "__main__":
    main()