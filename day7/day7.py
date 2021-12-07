# Import modules
import os
from termcolor import colored
import statistics

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [int(i) for i in inputFile.readline().split(',')]

    # Close the file and return the result
    inputFile.close()
    return input

# Puzzle 1
def puzzle1(filename):
    # Read file
    input = input_parser(filename)

    bestPos = int(statistics.median(input))

    return sum([abs(i - bestPos) for i in input])

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    minCost = 9999999999999999 # Ugly I know

    maxInput = max(input)

    for i in range(maxInput):
        minCost = min(minCost, sum([sum([x for x in range(abs(j - i)+1)]) for j in input]))
        print(str(i/maxInput*100) + '%')

    return minCost

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 37
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 168
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
