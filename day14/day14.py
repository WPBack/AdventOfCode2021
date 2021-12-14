# Import modules
import os
from termcolor import colored
from collections import Counter
import threading

# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    input = inputFile.readlines()
    template = list(input[0][:-1])
    rules = [line[:-1].split(' -> ') for line in input[2:]]

    # Close the file and return the result
    inputFile.close()
    return (template, rules)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (polymer, rules) = input_parser(filename)

    # Apply the rules 10 times
    for _ in range(10):
        oldPolymer = polymer.copy()
        polymerIdx = 0
        for oldPlymerIdx in range(len(oldPolymer)-1):
            twoChars = ''.join(oldPolymer[oldPlymerIdx:oldPlymerIdx+2])
            if twoChars in [rule[0] for rule in rules]:
                ruleIdx = [rule[0] for rule in rules].index(twoChars)
                polymer.insert(polymerIdx+1, rules[ruleIdx][1])
                polymerIdx += 2
            else:
                polymerIdx += 1

    # Count the number of occurances
    numOccurances = Counter(polymer).most_common()
    return numOccurances[0][1] - numOccurances[-1][1]

# Puzzle 2
def applyRules(polymer, rules):
    oldPolymer = polymer.copy()
    polymerIdx = 0
    for oldPlymerIdx in range(len(oldPolymer)-1):
        twoChars = ''.join(oldPolymer[oldPlymerIdx:oldPlymerIdx+2])
        if twoChars in [rule[0] for rule in rules]:
            ruleIdx = [rule[0] for rule in rules].index(twoChars)
            polymer.insert(polymerIdx+1, rules[ruleIdx][1])
            polymerIdx += 2
        else:
            polymerIdx += 1

# Puzzle 2 solver
def puzzle2(filename):
    # Read file
    (polymer, rules) = input_parser(filename)

    # Apply the rules 40 times
    for i in range(40):
        # Split the polymer into up to 12 parts for up to 12 threads
        if len(polymer) < 12:
            numThreads = len(polymer)
        else:
            numThreads = 12
        chunkSize = int(len(polymer)/numThreads)
        polymerChunks = [polymer[j:j+chunkSize].copy() for j in range(0, len(polymer), chunkSize)]

        # Process the chunks
        threads = []
        for j in range(len(polymerChunks)):
            threads.append(threading.Thread(target=applyRules, args=(polymerChunks[j], rules)))
            threads[j].start()

        # Wait for the threads to finnish and combine them
        threads[0].join()
        polymer = polymerChunks[0].copy()
        for j in range(1,len(polymerChunks)):
            threads[j].join()
            twoChars = polymer[-1] + polymerChunks[j][0]
            if twoChars in [rule[0] for rule in rules]:
                ruleIdx = [rule[0] for rule in rules].index(twoChars)
                polymer.append(rules[ruleIdx][1])
            polymer.extend(polymerChunks[j])


        print(str(i))

    # Count the number of occurances
    numOccurances = Counter(polymer).most_common()
    return numOccurances[0][1] - numOccurances[-1][1]

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 1588
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 1588
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
