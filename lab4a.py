# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

def is_even(lst):
    '''
    This will determine if a list has an even number in it.
    @param: A list
    @return: True or False
    '''
    for i in lst:
        if i % 2 == 0:
            return True
    return False        

x = [1, 3, 6, 7, 9, 12]

print(is_even(x))
