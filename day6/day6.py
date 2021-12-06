# Import modules
import os
from termcolor import colored

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
    fishes = input_parser(filename)

    # Simulate over 80 days
    for day in range(80):
        numNewFish = 0
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                numNewFish += 1
            else:
                fishes[i] -= 1
        fishes.extend([8]*numNewFish)

    return len(fishes)

# Puzzle 2
def puzzle2(filename):
    # Read file
    fishes = input_parser(filename)

    # Create a dictionary of how many fish have which timer
    fishesDict = [0]*9
    for i in range(9):
        fishesDict[i] = fishes.count(i)

    # Simulate over 256 days
    for day in range(256):
        numNewFish = fishesDict[0]
        for i in range(8):
            fishesDict[i] = fishesDict[i+1]
        fishesDict[8] = numNewFish
        fishesDict[6] += numNewFish

    return sum(fishesDict)

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 5934
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 26984457539
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
