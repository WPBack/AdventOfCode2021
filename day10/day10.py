# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [line[:-1] for line in inputFile.readlines()]

    # Close the file and return the result
    inputFile.close()
    return input

# Puzzle 1
def puzzle1(filename):
    # Read file
    input = input_parser(filename)
    
    points = 0
    for line in input:
        openChunks = []
        corrupt = False

        for bracket in line:
            if not corrupt:
                if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
                    openChunks.append(bracket)
                elif bracket == ')':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '(':
                        corrupt = True
                        points += 3
                elif bracket == ']':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '[':
                        corrupt = True
                        points += 57
                elif bracket == '}':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '{':
                        corrupt = True
                        points += 1197
                elif bracket == '>':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '<':
                        corrupt = True
                        points += 25137

    return points

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 26397
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
