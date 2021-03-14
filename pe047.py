from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
'''
def main():
    def primefactor(num):
        primefactors = []
        a = 2
        while num:
            if num%a == 0:
                primefactors.append(a)
            while num%a == 0:
                num //= a
            a += 1
            if a*a > num:
                primefactors.append(num)
                break
        return len(primefactors)
    
    consec = 0
    for i in count(647):
        numpf = primefactor(i)
        if numpf != 4:
            consec = 0
        elif numpf == 4:
            consec += 1
            if consec == 4:
                return i-3
        


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))