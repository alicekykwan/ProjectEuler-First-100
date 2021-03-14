from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''

'''
def count(r, c):
    return r*(r+1)*c*(c+1)//4
    ways = 0
    for rr in range(1, r+1):
        for cc in range(1, c+1):
            ways += (r-rr+1) * (c-cc+1)
    return ways

def main():
    closestways = float('inf')
    closestarea = 0
    for r in range(100):
        for c in range(100):
            ways = count(r,c)
            if abs(ways-2000000) < closestways:
                closestways = abs(ways-2000000)
                closestarea = r*c
    return closestarea

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))