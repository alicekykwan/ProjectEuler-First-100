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
f = open("p081_matrix.txt", "r")
a = f.read()
f.close()
print(a)

a = a.split('\n')
print(a)
b = [[int(numstr) for numstr in row.split(',')] for row in a]

def main():
    dp = [[None for _ in range(80)] for _ in range(80)]
    dp[0][0] = b[0][0]
    for c in range(1, 80):
        dp[0][c] = dp[0][c-1] + b[0][c]
    for r in range(1, 80):
        dp[r][0] = dp[r-1][0] + b[r][0]
    for r in range(1, 80):
        for c in range(1, 80):
            dp[r][c] = min([dp[r-1][c], dp[r][c-1]]) + b[r][c]
    
    print(dp[-1][-1])

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))