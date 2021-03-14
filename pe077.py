from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import PrimeSieve
'''
with open(".txt", "r") as f:
    a = f.read().split('\n')
'''

'''

'''
prime_sieve = PrimeSieve(10**5)
primes = prime_sieve.primes

def try_limit(limit):
    f = [0] * limit
    f[0]=1
    for prime in primes:
        if prime >= limit: break
        for i in range(prime, limit):
            f[i] += f[i-prime]
    for i in range(limit):
        if f[i] > 5000:
            return i
    return None



def main():
    curr = 10
    while True:
        res = try_limit(curr)
        if res is not None:
            print(res)
            break
        curr *= 2

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))