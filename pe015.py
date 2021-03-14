from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''


def main():
    dp = [[0]*21 for _ in range(21)]
    for i in range(21):
        dp[0][i] = 1
        dp[i][0] = 1
    
    for i in range(1, 21):
        for j in range(1, 21):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1]) 
    '''
    OR: 40 choose 20
    Binomial[40, 20]
    '''
start = time()
main()
print('Program took %.02f seconds' % (time()-start))