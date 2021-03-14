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
Mathematica:
Total[Total[IntegerDigits[Floor[Sqrt[#]*10^99]]]&/@Select[Range[100],Not[IntegerQ[Sqrt[#]]]&]]
'''
def bigsqrt_bsearch(x):
    a = 0
    b = x+1
    # a*a <= x < b*b
    while a+1<b:
        c = (a+b)//2
        if c*c<=x: a=c
        else: b=c
    return a

def bigsqrt_newton(a):
    x = a
    while True:
        y = (x + a//x) // 2
        #print(x,y)
        if y >= x: return x
        x = y

def f(n):
    # sqrt(n) * 10**99 = sqrt(n * 10**198)
    s = str(bigsqrt_newton(n*10**198))
    assert len(s) == 100
    return sum(int(d) for d in s)

def main():
    assert f(2) == 475
    squares = set(i*i for i in range(1, 10))
    print(sum(f(i) for i in range(1,100) if i not in squares))

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))