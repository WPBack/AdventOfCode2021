# Import modules
import os
from termcolor import colored

# Puzzle 1
def puzzle1(filename):
    # Read file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r') 
    input = inputFile.readlines()

    pos = 0
    depth = 0
    for line in input:
        dir = line[:-3]
        steps = int(line[-2])
        if dir == 'forward':
            pos += steps
        elif dir == 'down':
            depth += steps
        elif dir== 'up':
            depth -= steps

    return pos*depth


# Puzzle 2
def puzzle2(filename):
    # Read file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r') 
    input = inputFile.readlines()

    pos = 0
    depth = 0
    aim = 0
    for line in input:
        dir = line[:-3]
        steps = int(line[-2])
        if dir == 'forward':
            pos += steps
            depth += aim*steps
        elif dir == 'down':
            aim += steps
        elif dir== 'up':
            aim -= steps

    return pos*depth

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 150
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 900
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
