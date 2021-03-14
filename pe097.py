from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
'''
def powermod(a, b, m):
    # returns (a**b) % m
    # a^11 = a * a * ... * a
    #        a^1 * a^2 * a^8
    # a^2 = a*a
    # a^4 = a^2 * a^2
    # a^8 = a^4 * a^4
    currpow = a
    ans = 1
    while b:
        if b%2 == 1:
            ans = (ans * currpow) % m
        b //= 2
        currpow = (currpow * currpow) % m
    return ans

def main():
    m = 10**10
    print((28433*powermod(2, 7830457, m)+1)%m)
    power = 7830457
    ans = 1
    while power > 0:
        ans *= 2
        if ans > 10**10:
            ans %= 10**10
        power -= 1
    print((28433*ans+1)%10**10)

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))