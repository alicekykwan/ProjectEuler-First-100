from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
for each number
separate into digits
add up factorial of digits
if the sum is already seen, pull up the len and len of seen sums so far, record
if not seen, keep track of the sums
if the len is 60, increment count

'''
def main():
    f = [1]
    for i in range(1, 10):
        f.append(f[-1]*i)
    def digitfactsum(num):
        digits = []
        while num:
            digits.append(num%10)
            num//=10
        s = 0
        for digit in digits:
            s += f[digit]
        return s
    d = {}
    count = 0
    for i in range(1000000):
        seen = set()
        curr = i
        while curr not in d:
            seen.add(curr)
            nextnum = digitfactsum(curr)
            if nextnum in seen:
                d[i] = len(seen)
                break
            if nextnum in d:
                d[i] = len(seen) + d[nextnum]
                break
            curr = nextnum
        if d[i] == 60:
            count += 1
    print(count)



start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))