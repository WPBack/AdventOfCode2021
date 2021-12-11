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
# Recursive function that finds the size of a basin given the map, a point and the previous point (to not count that again)
def getBasinSize(map, checkedMap, row, col):
    checkedMap[row][col] = True
    # Check if we have a high point
    if map[row][col] == 9:
        return 0
    else:
        basinSize = 1
        # TODO: This probably must be replaced by a boolean map that keeps track on if a point is already included
        if row > 0 and not checkedMap[row-1][col]:
            basinSize += getBasinSize(map, checkedMap, row-1, col)
        if col < len(map[0])-1 and not checkedMap[row][col+1]:
            basinSize += getBasinSize(map, checkedMap, row, col+1)
        if row < len(map)-1 and not checkedMap[row+1][col]:
            basinSize += getBasinSize(map, checkedMap, row+1, col)
        if col > 0 and not checkedMap[row][col-1]:
            basinSize += getBasinSize(map, checkedMap, row, col-1)

        return basinSize

# Puzzle 2 solver
def puzzle2(filename):
    # Read file
    input = input_parser(filename)

    # Find all the lowpoints
    lowPoints = []
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
                lowPoints.append((row, col))

    # Find the size of each basin
    basinSizes = [0]*len(lowPoints)
    for i in range(len(lowPoints)):
        basinSizes[i] = getBasinSize(input, [[False]*len(input[0]) for _ in range(len(input))], lowPoints[i][0], lowPoints[i][1])

    # Sort the list and multipluy the last 3 elements
    basinSizes.sort()
    return basinSizes[-1]*basinSizes[-2]*basinSizes[-3]

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
puzzle2TestPass = puzzle2('example1') == 1134
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
