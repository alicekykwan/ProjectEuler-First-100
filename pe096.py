from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

with open("p096_sudoku.txt", "r") as f:
    a = f.read().split('Grid')
a = a[1:]
puzzles = []
for txt in a:
    puzzlebyrow = txt.split('\n')
    puzzlebyrow = puzzlebyrow[1:len(puzzlebyrow)-1]
    puzzle = [list(int(element) for element in row) for row in puzzlebyrow]
    assert(len(puzzle)==9)
    puzzles.append(puzzle)  

test = puzzles[0]

def solve(puzzle):  #no guess and test

    rowneeds = [set([1,2,3,4,5,6,7,8,9]) for _ in range(9)]
    colneeds = [set([1,2,3,4,5,6,7,8,9]) for _ in range(9)]
    gridneeds = [[set([1,2,3,4,5,6,7,8,9]) for _ in range(3)] for _ in range(3)]

    def update(i,j):
        #when the cell puzzle[i][j] is deteremed to be a single number, remove that number from rowneeds, colneeds, and gridneeds
        currnum = puzzle[i][j]
        rowneeds[i].discard(currnum)
        colneeds[j].discard(currnum)
        gridneeds[i//3][j//3].discard(currnum)

    for i in range(9):
        for j in range(9):
            update(i, j)
    
    while not (all(len(rowneed) == 0 for rowneed in rowneeds) and all(len(colneed)==0 for colneed in colneeds)):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j]: continue
                possibilities = rowneeds[i] & colneeds[j] & gridneeds[i//3][j//3]
                if len(possibilities) == 1:
                    print(i,j, possibilities)
                    puzzle[i][j] = list(possibilities)[0]
                    update(i,j)
            

def guessandtest(puzzle):
    '''
    try the first value in the list of possibilities,
    update function will take another argument (cell, possnum)
    
    toguess = [list of cells]
    def guess(toguess[i]):
        if i = len(toguess): return puzzle
        possibilities = list(rowneeds[i] & colneeds[j] & gridneeds[i//3][j//3])
        if len(possibilities) == 0: return
        for possnum in possibilities:
            update(toguess[i], possnum)
            a = guess(toguess[i+1]) 
            if a: return a
            undo(togiess[i], possnum)
    '''
    rowneeds = [set([1,2,3,4,5,6,7,8,9]) for _ in range(9)]
    colneeds = [set([1,2,3,4,5,6,7,8,9]) for _ in range(9)]
    gridneeds = [[set([1,2,3,4,5,6,7,8,9]) for _ in range(3)] for _ in range(3)]

    def update(i,j, possnum):
        #when the cell puzzle[i][j] is deteremed to be a single number, remove that number from rowneeds, colneeds, and gridneeds
        puzzle[i][j] = possnum
        rowneeds[i].discard(possnum)
        colneeds[j].discard(possnum)
        gridneeds[i//3][j//3].discard(possnum)

    def undo(i, j, possnum):
        puzzle[i][j] = 0
        rowneeds[i].add(possnum)
        colneeds[j].add(possnum)
        gridneeds[i//3][j//3].add(possnum)
    
    toguess = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]:
                update(i, j, puzzle[i][j])
            else:
                toguess.append((i, j))
    
    #print(toguess)
    def guess(toguessindex):
        if toguessindex == len(toguess):
            return puzzle
        i, j = toguess[toguessindex]
        possibilities = list(rowneeds[i] & colneeds[j] & gridneeds[i//3][j//3])
        if len(possibilities) == 0: return
        for possnum in possibilities:
            update(i,j, possnum)
            a = guess(toguessindex+1) 
            if a: return a
            undo(i,j, possnum)
    
    return guess(0)


def main():
    print('HELLO WORLD')
    #guessandtest(puzzles[1])
    ans = 0
    for i in range(50):
        solved = guessandtest(puzzles[i])
        code = 0
        for i in range(3):
            code*=10
            code+=solved[0][i]
        print(code)
        ans += code
    print(ans)

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))