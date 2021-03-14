from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

def main():
    def generateprimes(limit):
        primes = [2]
        def isPrime(num):
            for p in primes:
                if p**2 > num:
                    break
                if num%p == 0:
                    return False
            return True
        for i in range(3, limit, 2):
            if isPrime(i):
                primes.append(i)
        return set(primes)
    
    p = generateprimes(2000000)
    best = 0
    bestab = 0
    for a in range(-999,1000): 
        for b in range(-1000, 1001):
            numprimes = 0
            n = 0
            while True:
                if (n*n + a*n + b) in p:
                    numprimes += 1
                    n += 1
                else:
                    break
            if numprimes > best:
                best = numprimes
                bestab = a*b
    print(bestab)





start = time()
main()
print('Program took %.02f seconds' % (time()-start))