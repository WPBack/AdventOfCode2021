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
# Check flash function. Checks if the given row and col should flash and flashes adjacent if it should
def checkFlash(map, flashMap, row, col):
    nrFlashes = 0
    if map[row][col] > 9 and not flashMap[row][col]:
        nrFlashes += 1
        flashMap[row][col] = True
        if row > 0 and col > 0:
            map[row-1][col-1] += 1
            nrFlashes += checkFlash(map, flashMap, row-1, col-1)
        if row > 0:
            map[row-1][col] += 1
            nrFlashes += checkFlash(map, flashMap, row-1, col)
        if row > 0 and col < len(map[0])-1:
            map[row-1][col+1] += 1
            nrFlashes += checkFlash(map, flashMap, row-1, col+1)
        if col < len(map[0])-1:
            map[row][col+1] += 1
            nrFlashes += checkFlash(map, flashMap, row, col+1)
        if row < len(map)-1 and col < len(map[0])-1:
            map[row+1][col+1] += 1
            nrFlashes += checkFlash(map, flashMap, row+1, col+1)
        if row < len(map)-1:
            map[row+1][col] += 1
            nrFlashes += checkFlash(map, flashMap, row+1, col)
        if row < len(map)-1 and col > 0:
            map[row+1][col-1] += 1
            nrFlashes += checkFlash(map, flashMap, row+1, col-1)
        if col > 0:
            map[row][col-1] += 1
            nrFlashes += checkFlash(map, flashMap, row, col-1)
    
    return nrFlashes

# Puzzle 1 solver
def puzzle1(filename):
    # Read file
    input = input_parser(filename)

    # Simulate for 100 steps and count the number of flashes
    nrFlashes = 0
    for _ in range(100):
        flashMap = [[False]*len(input[0]) for _ in range(len(input))]

        # Increase all by 1
        for row in range(len(input)):
            for col in range(len(input[0])):
                input[row][col] += 1

        # Check flashes
        for row in range(len(input)):
            for col in range(len(input[0])):
                nrFlashes += checkFlash(input, flashMap, row, col)
        
        # 0 all that flashed
        for row in range(len(input)):
            input[row] = [0 if octopus > 9 else octopus for octopus in input[row]]

    return nrFlashes

# Puzzle 2
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 1656
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
