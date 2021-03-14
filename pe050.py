from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import Primes, PrimeSieve

'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def main():
    primes = Primes.primesieve(1000000)
    
    def findlongestconsecutive(targetprime):
        l = r = 0
        curr = 0
        while primes[r] < targetprime:
            if curr == targetprime:
                return r - l
            if curr < targetprime:
                curr += primes[r]
                r += 1
            elif curr > targetprime:
                if r-l < longestsum: break
                curr -= primes[l]
                l += 1
        return 1

    bestprime = 0
    longestsum = 0
    for prime in primes:
        sumlen = findlongestconsecutive(prime) 
        if sumlen > longestsum:
            bestprime = prime
            longestsum = sumlen
    print(bestprime, longestsum)


def other(limit=1000000):
    primesieve = PrimeSieve(limit)
    sieve = primesieve.sieve
    primes = primesieve.primes

    # Find largest window
    total = window = 0
    while total + primes[window] < limit:
        total += primes[window]
        window += 1

    while window > 0:
        # roll window
        total = sum(primes[i] for i in range(window))
        i = window
        while total < limit and i < len(primes):
            if sieve[total]: return total
            total += primes[i]
            total -= primes[i-window]
            i += 1
        window -= 1
        



start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))

start = time()
print('\n\n')
print(other())
print('Program took %.02f seconds' % (time()-start))