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
factor_sieve = FactorSieve(10**7)
prime_sieve = PrimeSieve(10**7)
sieve = prime_sieve.sieve
primes = prime_sieve.primes


def isPerm(num1,num2):
    return sorted(str(num1)) == sorted(str(num2))

def main():
    lowest = float('inf')
    lowestn = 0
    for i in range(2, 10**7):
        tot = factor_sieve.factor(i).totient()
        if isPerm(i, tot):
            if i/tot < lowest:
                lowest = i/tot
                lowestn = i
    return lowestn




start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))