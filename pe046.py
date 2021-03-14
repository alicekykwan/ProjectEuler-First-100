from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve

'''
It was proposed by Christian Goldbach that every odd composite number can be written as 
the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def main():
    primesieve = PrimeSieve(1000000)
    sieve = primesieve.sieve
    primes = primesieve.primes
    for i in count(35,2):
        if sieve[i]: #if this odd number is prime
            continue
        for j in count(1):
            if i - 2*j*j < 0: return i
            if sieve[i - 2*j*j]: break

    return "not found"

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))