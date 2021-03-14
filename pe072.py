from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve, FactorSieve

'''

'''
factor_sieve = FactorSieve(10**6+1)

def main():
    ans = 0
    for i in range(2, 1000001):
        ans += factor_sieve.factor(i).totient()
    return ans

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))