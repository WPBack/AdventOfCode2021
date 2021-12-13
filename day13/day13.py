# Import modules
import os
from termcolor import colored

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = inputFile.read().split('\n\n')
    dots = [[int(num) for num in dot.split(',')] for dot in input[0].split('\n')]
    width = max([dot[0] for dot in dots])+1
    height = max([dot[1] for dot in dots])+1
    sheet = [[False]*width for _ in range(height)]
    for dot in dots:
        sheet[dot[1]][dot[0]] = True
    foldsHorizontal = [instruction[11] == 'y' for instruction in input[1].split('\n')[:-1]]

    # Close the file and return the result
    inputFile.close()
    return (sheet, foldsHorizontal)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (sheet, foldsHorizontal) = input_parser(filename)
    
    # Fold the sheet once
    width = len(sheet[0])
    height = len(sheet)
    if foldsHorizontal[0]:
        prevHeight = height
        height = int(height/2)
        for y in range(height):
            for x in range(width):
                sheet[y][x] = sheet[y][x] or sheet[prevHeight-1-y][x]

    else:
        prevWidth = width
        width = int(width/2)
        for x in range(width):
            for y in range(height):
                sheet[y][x] = sheet[y][x] or sheet[y][prevWidth-1-x]
    
    return sum([sum(row[:width]) for row in sheet[:height]])

# Puzzle 2
def puzzle2(filename):
    # Read file
    (sheet, foldsHorizontal) = input_parser(filename)
    
    # Fold the sheet
    width = len(sheet[0])
    height = len(sheet)
    for fold in foldsHorizontal:
        if fold:
            prevHeight = height
            height = int(height/2)
            for y in range(height):
                for x in range(width):
                    sheet[y][x] = sheet[y][x] or sheet[prevHeight-1-y][x]

        else:
            prevWidth = width
            width = int(width/2)
            for x in range(width):
                for y in range(height):
                    sheet[y][x] = sheet[y][x] or sheet[y][prevWidth-1-x]

    # Convert the sheet to a string that can be printed
    result = ''
    for y in range(height):
        for x in range(width):
            if sheet[y][x]:
                result += '#'
            else:
                result += '.'
        result += '\n'
    return result[:-1]

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 17
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2sol = '#####\n#...#\n#...#\n#...#\n#####\n.....\n.....'
puzzle2TestPass = puzzle2('example1') == puzzle2sol
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: \n' + str(puzzle2('input')))
