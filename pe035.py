from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def main():
    '''
    n=10**6
    sieve = [True]*n
    sieve[0] = sieve[1] = False
    for p in range(2, n):
        if p*p>n: break
        if not sieve[p]: continue
        for i in range(p*p, n, p): sieve[i] = False
    primes=set(i for i in range(2,n) if sieve[i])
    '''
    primes = [2]
    def isPrime(i):
        for p in primes:
            if p * p > i: break
            if i%p == 0: return False
        return True
    for i in range(3, 1000000,2):
        if isPrime(i):
            primes.append(i)
    
    primes=set(primes)

    def makecircular(num):
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        digits.reverse()
        rotations = []
        n = len(digits)
        for i in range(n):
            rotations.append(digits[i:] + digits[:i])
        ans = []
        for rotation in rotations:
            num = 0
            for digit in rotation:
                num *= 10
                num += digit
            ans.append(num)
        return ans
    
    ans = 0
    lst = []
    for i in range(2, 1000000):
        if i in primes:
            if all(rotated in primes for rotated in makecircular(i)):
                ans += 1
                lst.append(i)
    
    print(ans)
    print(lst)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))