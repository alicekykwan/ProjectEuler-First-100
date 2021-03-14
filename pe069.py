from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import FactorSieve

'''

'''
def main():
    print(2*3*5*7*11*13*17)
    factorsieve = FactorSieve(10**6+1)
    r = (0, 0)
    for i in range(1, 10**6+1):
        j = factorsieve.factor(i).totient()
        r = max(r, (i/j, i))
    print(r)


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))