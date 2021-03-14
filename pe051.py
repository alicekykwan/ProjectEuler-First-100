from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve

'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
def main():
    primesieve = PrimeSieve(1000000)
    primes = primesieve.primes
    sieve = primesieve.sieve

    def tryreplace(num):
        onum = num
        digits = []
        while num:
            digits.append(num%10)
            num//=10
        c = Counter(digits)
        for digit, ct in c.items():
            if ct > 1:
                familyct = 1
                for i in range(digit+1, 10):
                    trynum = int(str(onum).replace(str(digit), str(i)))
                    if sieve[trynum]:
                        familyct += 1
                if familyct == 8:
                    return onum


    for prime in primes:
        c = Counter([int(num) for num in list(str(prime))])
        if any(ct > 1 for ct in c.values()):
            res = tryreplace(prime)
            if res:
                return res

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))