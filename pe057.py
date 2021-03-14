from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''

'''
def main():
    numer = 3
    denom = 2
    it = 1
    def nextiter(numer, denom):
        #add one to the previous term
        numer += denom
        # flip
        numer, denom = denom, numer
        # add one to curr term
        numer += denom
        return numer, denom
    def digitlen(num):
        l = 0
        while num:
            num //= 10
            l += 1
        return l

    ans = 0
    while it < 1000:
        numer, denom = nextiter(numer, denom)
        if digitlen(numer) > digitlen(denom):
            ans += 1
        it += 1
    print(ans)


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))