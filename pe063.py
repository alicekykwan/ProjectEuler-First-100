from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
The 5-digit number, 16807=75, is also a fifth power. 
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
def main():
    '''
    power gain rate is always 1
    if power < num digits, need digit gain rate to be < 1, meaning base <10
    => this means all ans are below 10 base
    if power > num digits, need digit gain rate to be > 1, meaning base > 10
    '''
    def findlen(num):
        l = 0
        while num:
            l += 1
            num //= 10
        return l
    ans = []
    for i in range(1, 10):
        currnum = i
        power = 1
        digitlen = 1
        while power == digitlen:
            ans.append(currnum)
            power += 1
            currnum *= i
            digitlen = findlen(currnum)
    print(ans, len(ans))


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))