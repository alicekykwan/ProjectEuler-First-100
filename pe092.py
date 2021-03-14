from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
def main():
    memo = set([89])
    memoone = set([1])
    def chain(num):
        curr = num
        past = set()
        while curr not in past:
            if curr in memo:
                memo.update(past)
                return 89
            if curr in memoone:
                memoone.update(past)
                return 1
            past.add(curr)
            digits = []
            while curr:
                digits.append(curr%10)
                curr//=10
            curr = sum(digit**2 for digit in digits)
        

    ans = 0
    for i in range(1, 10000000):
        if chain(i) == 89:
            ans += 1
    return ans

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))