from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import Fraction
from math import *

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def main():
    def primesieve(n):
        sieve = [True]*n
        sieve[0] = sieve[1] = False
        for p in range(2, n):
            if p*p>n: break
            if not sieve[p]: continue
            for i in range(p*p, n, p): sieve[i] = False
        primes=[i for i in range(2,n) if sieve[i]]
        return primes
    
    primes = primesieve(100000)

    def isPrime(num):
        for p in primes:
            if p**2 > num:
                break
            if num%p == 0:
                return False
        return True

    candidates = []
    for i in range(3, 8): #8 and 9 are impossible bcause sum of digits divisible by 9
        nums = [str(j) for j in range(1, i+1)]
        pers = permutations(nums)
        for per in pers:
            candidates.append(int(''.join(per)))
    
    pandigitalprimes = []

    for candidate in candidates:
        if isPrime(candidate):
            pandigitalprimes.append(candidate)
    
    print(max(pandigitalprimes))

start = time()
print('\n\n\n')
main()
print('Program took %.02f seconds' % (time()-start))