from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve
with open("p083_matrix.txt", "r") as f:
    a = f.read().split('\n')
b = [[int(ele)for ele in row.split(',')] for row in a]
test = [[131, 673, 234, 103, 18],[201, 96, 342, 965, 150],[630, 803, 746, 422, 111],[537, 699, 497, 121, 956],[805, 732, 524, 37,331]]

def main():
    print('HELLO WORLD')
    n = 80
    unvisited = set()
    dist = {}
    for r in range(n):
        for c in range(n):
            unvisited.add((r,c))
            dist[(r,c)] = float('inf')
    dist[(0,0)] = b[0][0]
    curr = (0,0)
    while unvisited:
        cr, cc = curr
        for nr, nc in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
            if 0 <= nr < n and 0 <= nc < n:
                ndist = dist[curr] + b[nr][nc]
                dist[(nr, nc)] = min(dist[(nr, nc)], ndist)
        #print(unvisited, len(unvisited))
        unvisited.remove(curr)
        if curr == (n-1, n-1): return dist[(n-1, n-1)]
        nextcurr = None
        nextcurrdist = float('inf')
        for grid, d in dist.items():
            if grid in unvisited and d < nextcurrdist:
                nextcurrdist = d
                nextcurr = grid
                #print(nextcurr, nextcurrdist)
        curr = nextcurr


    
    

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))