# Import modules
import os
from termcolor import colored

# Line class
class Line:
    def __init__(self, lineString):
        pointStrings = lineString.split(' -> ')
        self.x1 = int(pointStrings[0].split(',')[0])
        self.y1 = int(pointStrings[0].split(',')[1])
        self.x2 = int(pointStrings[1].split(',')[0])
        self.y2 = int(pointStrings[1].split(',')[1])

    def isHorizontal(self):
        return self.y1 == self.y2

    def isVertical(self):
        return self.x1 == self.x2

    def getPointsOnLine(self, considerDiagonal):
        if self.isHorizontal():
            return [(x, self.y1) for x in range(min(self.x1, self.x2), max(self.x1, self.x2)+1)]
        elif self.isVertical():
            return [(self.x1, y) for y in range(min(self.y1, self.y2), max(self.y1, self.y2)+1)]
        elif considerDiagonal:
            x = list(range(min(self.x1, self.x2), max(self.x1, self.x2)+1))
            y = list(range(min(self.y1, self.y2), max(self.y1, self.y2)+1))
            if (self.x2 > self.x1) != (self.y2 > self.y1):
                y.reverse()
            return list(zip(x, y))

        else:
            return []

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = [Line(lineString[:-1]) for lineString in inputFile.readlines()]

    # Close the file and return the result
    inputFile.close()
    return input

# Puzzle 1
def puzzle1(filename):
    # Read file
    lines = input_parser(filename)

    # Fill in the diagram
    diagramNRows = max(max([line.y1 for line in lines]), max([line.y2 for line in lines]))+1
    diagramNCols = max(max([line.x1 for line in lines]), max([line.x2 for line in lines]))+1
    diagram = [[0]*diagramNCols for i in range(diagramNRows)]
    for line in lines:
        for point in line.getPointsOnLine(False):
            diagram[point[1]][point[0]] += 1

    # Count the number of points with >=2 lines
    numOverlapping = 0
    for row in diagram:
        for point in row:
            if point >= 2:
                numOverlapping += 1

    return numOverlapping

# Puzzle 2
def puzzle2(filename):
    # Read file
    lines = input_parser(filename)

    # Fill in the diagram
    diagramNRows = max(max([line.y1 for line in lines]), max([line.y2 for line in lines]))+1
    diagramNCols = max(max([line.x1 for line in lines]), max([line.x2 for line in lines]))+1
    diagram = [[0]*diagramNCols for i in range(diagramNRows)]
    for line in lines:
        for point in line.getPointsOnLine(True):
            diagram[point[1]][point[0]] += 1

    # Count the number of points with >=2 lines
    numOverlapping = 0
    for row in diagram:
        for point in row:
            if point >= 2:
                numOverlapping += 1

    return numOverlapping

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 5
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 12
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
