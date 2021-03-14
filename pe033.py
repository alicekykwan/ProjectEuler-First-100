from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import Fraction
from math import *
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
'''

def main():
    curious = []
    for i in range(10,100): #denominator
        for j in range(10,100): #numerator
            if j >= i: break
            ddigits = list(str(i))
            ndigits = list(str(j))
            common = []
            ndigitscopy = ndigits[:]
            for digit in ddigits:
                if digit in ''.join(ndigitscopy):
                    ndigitscopy.remove(digit)
                    common.append(digit)
            if not common: continue
            if len(common) == 2: continue
            if common[0] == '0': continue
            for digit in common:
                ddigits.remove(digit)
                ndigits.remove(digit)
            dint = int(''.join(ddigits))
            nint = int(''.join(ndigits))
            if j*dint == i*nint:
                curious.append((j, i, nint, dint))
    print (curious)
                    
                    
def other():
    found = defaultdict(list)
    for a in range(1, 10):
        for b in range(a+1, 10):
            for x in range(1, 10):
                for aa in 10*a+x, 10*x+a:
                    for bb in 10*b+x, 10*x+b:
                        if a*bb!=aa*b: continue
                        print('%d/%d = %d/%d' % (a, b, aa, bb))
                        found[(aa, bb)].append(Fraction(a, b))
    answer = 1
    for lst in found.values():
        for elem in lst: answer *= elem
    print(answer)
    
start = time()
other()
print('Program took %.02f seconds' % (time()-start))
    
start = time()
main()
print('Program took %.02f seconds' % (time()-start))