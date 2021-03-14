
from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def main():
    ans = 1
    for i in range(3, 1002, 2):
        upperright = i*i
        upperleft = upperright - (i-1)
        lowerleft = upperleft - (i-1)
        lowerright = lowerleft - (i-1)
        ans += upperright + upperleft + lowerleft + lowerright
    print(ans)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))