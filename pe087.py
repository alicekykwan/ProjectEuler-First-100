from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve, sqrt
'''

'''
n = 5*10**7
a = PrimeSieve(sqrt(n)).primes

def main():
    ans = set()
    for i in a:
        ii=i*i
        for j in a:
            jjj=j*j*j
            if ii+jjj >= n: break
            for k in a:
                s = ii+jjj+k*k*k*k
                if  s < n:
                    ans.add(s)
                else: 
                    break
    print(len(ans))

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))
