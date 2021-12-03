# Import modules
import os
from termcolor import colored
import numpy as np

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [[b == '1' for b in line[:-1]] for line in inputFile.readlines()]

    # Close the file and return the result
    inputFile.close()
    return input

# Puzzle 1
def puzzle1(filename):
    # Read file
    input = input_parser(filename)

    # Calculate gamma and epsilon
    numTrue = np.sum(input, axis=0)
    gammaBin = [num > len(input)/2 for num in numTrue]
    epsilonBin = np.invert(gammaBin)
    gamma = int(''.join(['1' if b else '0' for b in gammaBin]), 2)
    epsilon = int(''.join(['1' if b else '0' for b in epsilonBin]), 2)

    return gamma*epsilon

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 198
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
