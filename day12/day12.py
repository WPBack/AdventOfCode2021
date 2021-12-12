# Import modules
import os
from termcolor import colored

# Cave class
class Cave:
    def __init__(self, caveString):
        self.name = caveString
        self.small = caveString[0].islower()
        self.connections = []

    def __str__(self):
        return self.name + str([connection.name for connection in self.connections])
        

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [line[:-1].split('-') for line in inputFile.readlines()]
    caves = [Cave('start')]
    for connection in input:
        # Find the caves and add them if they do not exist
        cave1Id = 0
        cave2Id = 0
        cave1Found = False
        cave2Found = False
        for i in range(len(caves)):
            if caves[i].name == connection[0]:
                cave1Found = True
                cave1Id = i
            elif caves[i].name == connection[1]:
                cave2Found = True
                cave2Id = i
        if not cave1Found:
            caves.append(Cave(connection[0]))
            cave1Id = len(caves)-1
        if not cave2Found:
            caves.append(Cave(connection[1]))
            cave2Id = len(caves)-1

        # Add the connection
        caves[cave1Id].connections.append(caves[cave2Id])
        caves[cave2Id].connections.append(caves[cave1Id])

    # Close the file and return the result
    inputFile.close()
    return caves

# Puzzle 1
# Recursively count the number of paths
def getNumPathsToEnd(start, path):
    if start.name == 'end':
        return 1
    
    if start.small and start in path:
        return 0

    path.append(start)
    numPaths = 0
    for connection in start.connections:
        numPaths += getNumPathsToEnd(connection, path.copy())

    return numPaths

# Puzzle 1 solver
def puzzle1(filename):
    # Read file
    caves = input_parser(filename)

    # Count the number of ways to reach the end
    path = []
    return getNumPathsToEnd(caves[0], path.copy())

# Puzzle 2
# Recursively count the number of paths
def getNumPathsToEndPuzzle2(start, path, smallVisitedTwice):
    if start.name == 'end':
        return 1
    
    if start.name == 'start' or (start.small and start in path and smallVisitedTwice):
        return 0

    smallVisitedTwiceNow = smallVisitedTwice or (start.small and start in path)

    path.append(start)
    numPaths = 0
    for connection in start.connections:
        numPaths += getNumPathsToEndPuzzle2(connection, path.copy(), smallVisitedTwiceNow)

    return numPaths

# Puzzle 2 solver
def puzzle2(filename):
    # Read file
    caves = input_parser(filename)

    # Count the number of ways to reach the end
    path = []
    return sum([getNumPathsToEndPuzzle2(start, path.copy(), False) for start in caves[0].connections])

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 10 and puzzle1('example2') == 19 and puzzle1('example3') == 226
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 36 and puzzle2('example2') == 103 and puzzle2('example3') == 3509
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
