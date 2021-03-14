from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
Farey Sequence
k = (1000000-5)//7          this gives the highest denom under 1 mil
print (2+3*k, 5+7*k)

2/5                       3/7
        5/12
   7/19      8/19
                 ...
                 (2+3k)/(5+7k)
'''
def main():
    
    best = 0
    for d in range(1, 1000001):
        n = (3*d-1)//7
        best = max(best, Fraction(n, d))
    print(best, best.numerator)
    
start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))