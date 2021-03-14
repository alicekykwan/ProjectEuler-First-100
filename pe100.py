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
    print('HELLO WORLD')
    a = 7
    b = 5
    while (a+1//2) < 10**12:
        nexta = 3*a+4*b
        nextb = 2*a+3*b
        a = nexta
        b = nextb
    print((b+1)//2)


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))