# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

def is_even(lst):
    '''
    This will create a new list of just the even numbers of a provided list
    @param: A list
    @return: A new list of just even numbers
      '''
    y=[]
    for i in lst:
        if i % 2 == 0:
            y.append(i)
    return y      

x = [1, 3, 5, 7, 9, 11, 13, 15]

print(is_even(x))
