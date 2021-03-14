from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least 
two positive integers?
'''
def main():
    nums = [i for i in range(1,100)]
    dp = [0]*101
    dp[0] = 1
    
    
    for num in nums:
        for i in range(num, 101):
            dp[i] += dp[i-num]
    print(dp)
    print(dp[100]-1)
start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))