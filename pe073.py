from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
import sys
sys.setrecursionlimit(15000)

from pe_lib import FactorSieve

'''

'''
def slow(n):
    count = [0]
    def dfs(left, right):
        mid = Fraction(left.numerator+right.numerator, left.denominator+right.denominator)
        if mid.denominator > n:
            return
        count[0] += 1
        dfs(left, mid)
        dfs(mid, right)

    left = Fraction(1,3)
    right = Fraction(1,2)
    dfs(left, right)
    print(count)

# O(n^2/12)
def slow2(n):
    factor_sieve = FactorSieve(n+1)
    result = 0
    for d in range(4, n+1):
        # lower_bound     1    lower_bound+1
        # ----------- <=  - <  -------------
        #      d          3          d
        lower_bound = d//3
        # upper_bound    1     upper_bound+1
        # ----------- <  - <=  -------------
        #      d         2           d
        upper_bound = (d-1)//2
        for i in range(lower_bound+1, upper_bound+1):
            if gcd(i, d) == 1:
                result += 1
    return result

def fast(n):
    factor_sieve = FactorSieve(n+1)
    result = 0
    for d in range(4, n+1):
        # lower_bound     1    lower_bound+1
        # ----------- <=  - <  -------------
        #      d          3          d
        lower_bound = d//3
        # upper_bound    1     upper_bound+1
        # ----------- <  - <=  -------------
        #      d         2           d
        upper_bound = (d-1)//2
        divisors = [1]
        for p, _ in factor_sieve.factor(d):
            divisors += [i*-p for i in divisors]
        for i in divisors:
            s = 1
            if i < 0:
                i = abs(i)
                s = -1
            result += s * (upper_bound//i - lower_bound//i)
        '''
        + divisible by 1 = 5998 - 3999
        - divisible by 3 = 5998//3 - 3999//3
        - divisible by 31 = 5998//31 - 3999//31
        - divisible by 43 = 5998//43 - 3999//43
        + divisible by 3*31 = 5998//(3*31) - 3999//(3*31)
        + divisible by 3*43 = 5998//(3*43) - 3999//(3*43)
        + divisible by 31*43 = 5998//(31*43) - 3999//(31*43)
        - divisible by 3*31*43
        (3999, 5998]
        totient of i 
        = total number of reduced proper fractions with i as denom
        '''
    return result


def main():
    #print(slow(12000))
    #print(slow2(12000))
    print(fast(12000))
    #print(fast(10**6)) #50660592050
    


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))