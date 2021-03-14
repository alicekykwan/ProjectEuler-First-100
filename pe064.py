from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

from pe_lib import sqrt



''' 
    c <= a + b sqrt(n)
    c-a <= b sqrt(n)
    if c-a negative then check (c-a)^2 >= b^2 n
    if c-a positive then check (c-a)^2 <= b^2 n
'''
def nxt(a, b, n): # a+b*(n**0.5)
        c = int((a+b*(n**0.5))//1) # probably where it will fail for large n
        d = (a-c)**2 - (b**2)*n
        newa = Fraction(a-c, d)
        newb = Fraction(-b, d)
        return (newa, newb, n, c)
        
def findperiod(n):
    a, b = 0, 1
    target = -1
    cf = []
    while True:
        a, b, n, c = nxt(a, b, n)
        if target < 0: target = 2*c
        cf.append(c)
        if c == target: break
    return len(cf)-1

def isSquare(num):
    if sqrt(num)**2 == num:
        return True

def main():
    ans = 0
    for i in range(2, 10001):
        if isSquare(i): continue
        if findperiod(i) % 2: ans += 1
    return ans

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))