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

    # Complete the incomplete lines and count score
    scores = []
    for lineNr in range(len(input)):
        openChunks = []
        corrupt = False

        for bracket in input[lineNr]:
            if not corrupt:
                if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
                    openChunks.append(bracket)
                elif bracket == ')':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '(':
                        corrupt = True
                elif bracket == ']':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '[':
                        corrupt = True
                elif bracket == '}':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '{':
                        corrupt = True
                elif bracket == '>':
                    lastOpen = openChunks.pop()
                    if not lastOpen == '<':
                        corrupt = True
        
        if not corrupt:
            score = 0
            for openChunk in reversed(openChunks):
                score *= 5
                if openChunk == '(':
                    score += 1
                elif openChunk == '[':
                    score += 2
                elif openChunk == '{':
                    score += 3
                elif openChunk == '<':
                    score += 4

            scores.append(score)

    return statistics.median(scores)

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
puzzle2TestPass = puzzle2('example1') == 288957
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
