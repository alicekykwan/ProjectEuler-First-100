from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import PrimeSieve

'''
Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals 
are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral 
for which the ratio of primes along both diagonals first falls below 10%?
'''
def main():
    primesieve = PrimeSieve(1000000)
    primes = primesieve.primes
    def isPrime(num):
        for p in primes:
            if p**2 > num:
                break
            if num%p == 0:
                return False
        return True
    allcount = 13
    primecount = 8
    currside = 7 
    while primecount/allcount >= 0.1:
        currside += 2
        a = currside**2
        newcorners = [a, a-currside+1, a-2*currside+2, a-3*currside+3]
        for corner in newcorners:
            if isPrime(corner):
                primecount += 1
        allcount += 4
    print(currside)


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))