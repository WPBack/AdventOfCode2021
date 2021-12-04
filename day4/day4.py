# Import modules
import os
from termcolor import colored
import csv
import numpy as np

# Bingo board class
class BingoBoard:
    def __init__(self, boardString):
        self.board = [[0]*5 for i in range(5)]
        for row in range(5):
            for col in range(5):
                self.board[row][col] = int(boardString.split('\n')[row][col*3:col*3+2])

        self.marked = [[False]*5 for i in range(5)]

    def checkDraw(self, draw):
        marked = False
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == draw:
                    self.marked[row][col] = True
                    marked = True

        if marked:
            for row in range(5):
                bingoRow = True
                for col in range(5):
                    if not self.marked[row][col]:
                        bingoRow = False
                if bingoRow:
                    return True
            
            for col in range(5):
                bingoCol = True
                for row in range(5):
                    if not self.marked[row][col]:
                        bingoCol = False
                if bingoCol:
                    return True

        return False

    def getSumOfUnmarked(self):
        return sum(map(sum, self.board*np.invert(self.marked)))
                


# Input parser
def input_parser(filename):
    # Open the file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputFile = open(os.path.join(__location__, filename), 'r')

    # Process the file
    draws = [int(i) for i in inputFile.readline()[:-1].split(',')]
    bingoBoards = [BingoBoard(board) for board in inputFile.read()[1:].split('\n\n')]

    # Close the file and return the result
    inputFile.close()
    return (draws, bingoBoards)

# Puzzle 1
def puzzle1(filename):
    # Read file
    (draws, bingoBoards) = input_parser(filename)
    for draw in draws:
        for board in bingoBoards:
            bingo = board.checkDraw(draw)
            if bingo:
                return board.getSumOfUnmarked()*draw

    print('No bingo found!')
    return 0

# Puzzle 2
def puzzle2(filename):
    # Read file
    (draws, bingoBoards) = input_parser(filename)
    numBoards = len(bingoBoards)
    numBingos = 0
    for draw in draws:
        for board in list(bingoBoards):
            bingo = board.checkDraw(draw)
            if bingo:
                numBingos += 1
                if numBingos == numBoards:
                    return board.getSumOfUnmarked()*draw
                bingoBoards.remove(board)

    print('Did not bingo on all boards')
    return 0

# Run tests for puzzle 1
puzzle1TestPass = puzzle1('example1') == 4512
if(puzzle1TestPass):
    print(colored('Tests for puzzle 1 PASS', 'green'))
else:
    print(colored('Tests for puzzle 1 FAIL', 'red'))

# Solve puzzle 1 if test passed
if(puzzle1TestPass):
    print('Solution for puzzle 1: ' + str(puzzle1('input')))

# Run tests for puzzle 2
puzzle2TestPass = puzzle2('example1') == 1924
if(puzzle2TestPass):
    print(colored('Tests for puzzle 2 PASS', 'green'))
else:
    print(colored('Tests for puzzle 2 FAIL', 'red'))

# Solve puzzle 2 if test passed
if(puzzle2TestPass):
    print('Solution for puzzle 2: ' + str(puzzle2('input')))
