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
    sequence = [1, 2]
    k = 2
    while len(sequence) < 100:
        sequence += [1, 1, 2*k]
        k += 1
    sequence = sequence[:99]
    print(sequence)

    it = 98
    numer = 1
    denom = sequence[it]
    
    while it > 0:
        it -= 1
        numer = sequence[it]*denom + numer
        numer, denom = denom, numer
    
    numer += 2*denom

    print(numer, denom)

    digitsum = 0
    while numer:
        digitsum += numer%10
        numer//=10
    return digitsum

def other():
    sequence = [2]
    k = 1
    while len(sequence) <= 100:
        sequence += [1, 2*k, 1]
        k += 1
    sequence = sequence[:100]
    print(sequence)

    c = Fraction(sequence.pop(), 1)
    for elem in reversed(sequence):
        c = elem+1/c
    print(float(c))
    print(c)
    print(sum(int(d) for d in str(c.numerator)))

start = time()
print('\n\n')
print(other())
print('Program took %.02f seconds' % (time()-start))