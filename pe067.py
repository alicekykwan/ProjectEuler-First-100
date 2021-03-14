from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *


'''
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, 
as there are 299 altogether! If you could check one trillion (1012) routes 
every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)

'''

f = open("p067_triangle.txt", "r")
a = f.read()
f.close()
a = a.split('\n')

triangle = [[int(numstr) for numstr in row.split(' ')]
            for row in a]

def main():
    R = len(triangle)
    dp = [59]
    for i in range(1, R):
        nextdp = []
        C = len(triangle[i])
        for j in range(C):
            if j == 0:
                nextdp.append(dp[j] + triangle[i][j])
            elif j == C-1:
                nextdp.append(dp[j-1] + triangle[i][j])
            else:
                nextdp.append(max(dp[j-1], dp[j]) + triangle[i][j])
        dp = nextdp
    print(max(dp))



start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))