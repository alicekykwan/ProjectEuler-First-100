from collections import *
from itertools import *
from random import *
from time import *

'''
Find the sum of all the primes below two million.
'''

def main():
    primes = [2]
    def isPrime(num):
        for p in primes:
            if p**2 > num:
                break
            if num%p == 0:
                return False
        return True
    for i in range(3, 2000000, 2):
        if isPrime(i):
            primes.append(i)
    print(sum(primes))

start = time()
main()
print('Program took %.02f seconds' % (time()-start))