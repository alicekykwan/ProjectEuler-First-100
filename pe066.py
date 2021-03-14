from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import sqrt
'''
with open("p096_sudoku.txt", "r") as f:
    a = f.read().split('Grid')
'''

def makenext(a,c,D):
    newc = (D - a**2)//c
    newa = -a
    x = ((newa + sqrt(D))//newc)
    newa -= x*newc
    return x, newa, newc

def makesequence(D):
    floor = sqrt(D)
    seq = []
    a = -floor
    c = 1
    while True:
        x, aa, cc = makenext(a, c, D)
        seq.append(x)
        if x == 2*floor: break
        a = aa
        c = cc
    return chain([floor], cycle(seq))

def makeconvergents(seq):
    h0=0
    k0=1
    h1=1
    k1=0
    for i in seq:
        h = i*h1+h0
        k=i*k1+k0
        yield h, k
        h0,k0,h1,k1 = h1,k1,h,k

def findx(D):
    sqrtD = sqrt(D)
    if sqrtD * sqrtD == D:
        return 0
    seq = makesequence(D)
    for x, y in makeconvergents(seq):
        if x*x-D*y*y == 1:
            return x

def main():
    print(max(range(1, 1001), key=findx)) 



start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))