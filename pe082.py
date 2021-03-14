from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

with open("p082_matrix.txt", "r") as f:
    a = f.read().split('\n')
b = [[int(ele)for ele in row.split(',')] for row in a]
test = [[131, 673, 234, 103, 18],[201, 96, 342, 965, 150],[630, 803, 746, 422, 111],[537, 699, 497, 121, 956],[805, 732, 524, 37,331]]

def main():
    #0 = from left, 1 = from top, 2 = from bottom
    n = 80
    dp = [[[float('inf') for _ in range(n)] for _ in range(n)] for _ in range(3)]
    for r in range(n):
        dp[0][r][0] = b[r][0]
    '''
    dp[0][r][c] = min of:
    from left: min(dp[x][r][c-1] for x in range(3))
    from top: min(dp[x][r-1][c] for x in [0, 1]) if r-1 >=0
    from bot: min(dp[x][r+1][c] for x in range[0,2]) if r+1 < 80
    + b[r][c]

    need to compute from top and from bot
    when I have the min(dp[x][r][c]), I can push forward and compute:
    going right: dp[0][r][c+1], which is my value + b[r][c+1]
    going right then down: (fr top) dp[1][rr][c+1] for rr in range r+1, 80
        which is my value + each previous b[rr][c+1] including rr
        (initialize as my value + b[r][c+1])
    going right then up: (fr bot) dp[2][rr][c+1] for rr in range(r-1, -1, -1)
        which is my value + each previous b[rr][c+1]
        (initialize as my value + b[r][c+1])
    '''
    for c in range(n-1): #for each column
        for r in range(n):
            slf = min(dp[x][r][c] for x in range(3))
            slfandright = slf + b[r][c+1]
            dp[0][r][c+1] = slfandright
            currdown = slfandright
            for rr in range(r+1, n):
                if rr > n-1: break
                currdown += b[rr][c+1]
                dp[1][rr][c+1] = min(dp[1][rr][c+1], currdown)
            currup = slfandright
            for rr in range(r-1, -1, -1):
                if rr < 0: break
                currup += b[rr][c+1]
                dp[2][rr][c+1] = min(dp[2][rr][c+1], currup)
    
    print(dp)
    return min(dp[x][r][n-1] for x in range(3) for r in range(n))
start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))