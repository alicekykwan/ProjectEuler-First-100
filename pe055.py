from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
How many Lychrel numbers are there below ten-thousand?
'''
def main():
    def reverse(num):
        digits = []
        while num:
            digits.append(num%10)
            num //= 10
        ans = 0
        for digit in digits:
            ans *= 10
            ans += digit
        return ans
    def isPalin(num):
        a = list(str(num))
        return a == a[::-1]
    ans = []
    for i in range(1, 10000):
        it = 0
        currnum = i
        while it < 50:
            reverseandadd = currnum + reverse(currnum)
            if isPalin(reverseandadd):
                break
            else:
                currnum = reverseandadd
                it += 1
        if it == 50:
            ans.append(i)
    print(ans, len(ans))


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))