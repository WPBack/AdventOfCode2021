# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = inputFile.readlines()
    signalPatterns = [line.split(' | ')[0] for line in input]
    signalPatternsSplit = [patterns.split(' ') for patterns in signalPatterns]
    outputPatterns = [line[:-1].split(' | ')[1] for line in input]
    outputPatternsSplit = [patterns.split(' ') for patterns in outputPatterns]

    # Close the file and return the result
    inputFile.close()
    return (signalPatternsSplit, outputPatternsSplit)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (signalPatterns, outputPatterns) = input_parser(filename)

    # Count the number of outputs that should produce 1, 4, 7 or 8
    ouptutPatternLens = [[len(pattern) for pattern in patterns] for patterns in outputPatterns]
    numUnique = 0
    for outputPatternLen in ouptutPatternLens:
        for patternLen in outputPatternLen:
            if patternLen == 2 or patternLen == 4 or patternLen == 3 or patternLen == 7:
                numUnique += 1

    return numUnique

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 0 and puzzle1('example2') == 26
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
