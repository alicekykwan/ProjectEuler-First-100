from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import sqrt
'''
with open(".txt", "r") as f:
    a = f.read().split('\n')
'''

'''

'''
def main():
    print('HELLO WORLD')
    N = 1500000
    p = [0] * (N+1)
    for m in range(2, sqrt(N)):
        for n in range(1, m):
            if gcd(m,n) > 1: continue
            if m%2 and n%2: continue
            k = 1
            while k*(2*m*m+2*m*n) <= N:
                p[k*(2*m*m+2*m*n)] += 1
                k += 1
    ans = 0
    for count in p:
        if count == 1:
            ans += 1
    return ans

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))