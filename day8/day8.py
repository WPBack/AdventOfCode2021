# Import modules
import os
from termcolor import colored
import numpy as np

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
    return ([[[ord(i)-97 for i in j] for j in k] for k in signalPatternsSplit], [[[ord(i)-97 for i in j] for j in k] for k in outputPatternsSplit])

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
    (allSignalPatterns, allOutputPatterns) = input_parser(filename)

    result = 0
    for i in range(len(allSignalPatterns)):
        possiblePoses = [[j for j in range(7)] for k in range(7)]
        while(any([len(j) > 1 for j in possiblePoses])):
            for seg in range(7):
                numWithLen5 = 0
                numWithLen6 = 0
                for signalPattern in allSignalPatterns[i]:
                    if seg in signalPattern:
                        # 1
                        if len(signalPattern) == 2:
                            possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in [0, 1, 3, 4, 6]]
                        # 7
                        elif len(signalPattern) == 3:
                            possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in [1, 3, 4, 6]]
                        # 4
                        elif len(signalPattern) == 4:
                            possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in [0, 4, 6]]
                        # 2, 3 or 5
                        elif len(signalPattern) == 5:
                            # a, d and g must be in all of these
                            numWithLen5 += 1
                        # 0 or 6 or 9
                        elif len(signalPattern) == 6:
                            # a, b, f and g must be in all of these
                            numWithLen6 += 1
                        # 8 cannot remove anything
                if numWithLen5 != 3:
                    possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in [0, 3, 6]]
                if numWithLen6 != 3:
                    possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in [0, 1, 5, 6]]

            # All with length 1 should now be removed from all other lists
            for j in range(7):
                if len(possiblePoses[j]) == 1:
                    for seg in range(7):
                        if seg != j:
                            possiblePoses[seg] = [x for x in possiblePoses[seg] if not x in possiblePoses[j]]

        # Decode the ouptut pattern and add to the result! possiblePoses now contains which segment each signal corresponds to
        output = 0
        for j in range(len(allOutputPatterns[i])):
            num = 0
            if len(allOutputPatterns[i][j]) == 2:
                num = 1
            elif len(allOutputPatterns[i][j]) == 3:
                num = 7
            elif len(allOutputPatterns[i][j]) == 4:
                num = 4
            else:
                litSegments = [possiblePoses[sig][0] for sig in allOutputPatterns[i][j]]
                if len(litSegments) == 5:
                    if 4 in litSegments:
                        num = 2
                    elif 2 in litSegments:
                        num = 3
                    else:
                        num = 5
                elif len(litSegments) == 6:
                    if not 3 in litSegments:
                        num = 0
                    elif 4 in litSegments:
                        num = 6
                    else:
                        num = 9
                else:
                    num = 8
            output += num*pow(10, (3-j))

        result += output

    return result

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
puzzle2TestPass = puzzle2('example1') == 5353 and puzzle2('example2') == 61229
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
