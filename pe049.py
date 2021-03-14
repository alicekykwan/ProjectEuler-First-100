from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
def main():
    '''
    for each 4 digit prime
    find permutations of the 4 digits
    keep the permutations that are prime also; discard perms starting with 0
    sort the remaining 4 digit prime permutations
    for each permutation, find differences between it and larger permutations
        store the differences
        for each difference, see if there's one that's twice as big as it
    
    '''
    primesieve = PrimeSieve(10000)
    primes = primesieve.primes
    sieve = primesieve.sieve
    
    def permute(num):
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        pers = list(permutations(digits))
        primepers = set()
        for per in pers:
            if per[0] == 0: continue
            pervalue = 0
            for digit in per:
                pervalue *= 10
                pervalue += digit
            if sieve[pervalue]: 
                primepers.add(pervalue)
        primepers = list(primepers)
        primepers.sort()
        return primepers

    #ans = []
    ans = set()
    for prime in primes:
        if prime < 1000: continue
        primepers = permute(prime)
        n = len(primepers)
        for i in range(n):
            diffs = []
            for j in range(i+1, n):
                diffs.append(primepers[j]-primepers[i])
            diffset = set(diffs)
            for diff in diffs:
                if diff > 0 and 2*diff in diffset:
                    ans.add((primepers[i], primepers[i]+diff, primepers[i]+2*diff))

    return ans

'''    print(permute(1487))
    primepers = permute(1487)
    n = len(primepers)
    for i in range(n):
        diffs = []
        
        for j in range(i+1, n):
            diffs.append(primepers[j]-primepers[i])
        diffset = set(diffs)
        print(diffs, diffset)

        for diff in diffs:
            if 2*diff in diffset:
                print('found')
                print((primepers[i], primepers[i]+diff, primepers[i]+2*diff))     '''

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))