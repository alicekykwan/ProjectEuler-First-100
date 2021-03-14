from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from math import *
'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

# every hexagonal number is triangular
# only need to find hexagonal=pentagonal
def find_both(k=2):
    np = nh = 1
    p = h = 1
    while k > 0:
        if p == h:
            print(p)
            k -= 1
        if p <= h:
            np += 1
            p = pentagonal(np)
        else:
            nh += 1
            h = hexagonal(nh)


def main():
    p = [40755]
    h = [40755]
    tn = 286
    pn = 166
    hn = 144
    while True:
        tnum = tn*(tn+1)//2
        while p[-1] < tnum:
            p.append(pn*(3*pn-1)//2)
            pn += 1
        while h[-1] < tnum:
            h.append(hn*(2*hn-1))
            hn += 1
        if tnum == p[-1] and tnum == h[-1]:
            print (tnum)
            break
        tn += 1

    
start = time()
find_both(3)
print('Program took %.02f seconds' % (time()-start))

start = time()
print(main())
print('Program took %.02f seconds' % (time()-start))