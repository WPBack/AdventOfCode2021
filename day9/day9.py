# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [[int(num) for num in list(line[:-1])] for line in inputFile.readlines()]

    # Close the file and return the result
    inputFile.close()
    return input

# Puzzle 1
def puzzle1(filename):
    # Read file
    input = input_parser(filename)
    
    # Find the lowpoints and add up
    result = 0
    nRows = len(input)
    nCols = len(input[0])
    for row in range(nRows):
        for col in range(nCols):
            adjacent = [10]*4
            if not row == 0:
                adjacent[0] = input[row-1][col]
            if not col == nCols-1:
                adjacent[1] = input[row][col+1]
            if not row == nRows-1:
                adjacent[2] = input[row+1][col]
            if not col == 0:
                adjacent[3] = input[row][col-1]

            if input[row][col] < min(adjacent):
                result += input[row][col]+1

    return result

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 15
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 2
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
