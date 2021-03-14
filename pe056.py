from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''
def digitsum(num):
    digits = []
    while num:
        digits.append(num%10)
        num //= 10
    return sum(digits)

def main():
    best = 0
    for a in range(1, 100):
        for b in range(1, 100):
            best = max(best, digitsum(a**b))
    print(best)


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))