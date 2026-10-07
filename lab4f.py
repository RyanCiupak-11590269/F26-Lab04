# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: October 7, 2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

def get_initials(*args):
    initials = []
    for names in args:
        initials.append(names[0])
    return initials

def main():
    print(get_initials("John", "Doe"))
    print(get_initials("Jelyn", "Dom", "Yannah", "Danny", "Duncan", "Marissa"))

if __name__ == "__main__":
    main()