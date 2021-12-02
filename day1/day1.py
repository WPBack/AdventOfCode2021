# Import modules
import os
from termcolor import colored

# Puzzle 1
def puzzle1(filename):
    # Read file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r') 
    input = inputFile.readlines()

    numIncreases = 0
    for i in range(len(input)-1):
        if int(input[i+1]) > int(input[i]):
            numIncreases += 1

    return numIncreases


# Puzzle 2
def puzzle2(filename):
    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 7
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2

# Solve puzzle 2 if test passed