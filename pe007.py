from collections import *
from itertools import *
from random import *
from time import *


'''
What is the 10 001st prime number?
'''


def main():
    primes = [2]
    def test(num):
        for p in primes:
            if p * p > num: break
            if num % p == 0: return False
        return True
    for curr in count(3, 2):
        if test(curr):
            primes.append(curr)
            if len(primes) >= 10001:
                break

    print(primes[-1])

start = time()
main()
print('Program took %.02f seconds' % (time()-start))