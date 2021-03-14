from collections import *
from itertools import *
from random import *
from time import *


'''
What is the Longest Collatz sequence 
Which starting number, under one million, produces the longest chain?
n => n/2 for even n
n => 3n + 1 for odd n
'''

def main():
    memo = {1: 1}
    def findCollatzLen(num):
        originalnum = num
        if num in memo:
            return memo[num]
        ans = 1
        while num != 1:
            if num % 2: 
                num = 3*num + 1
            else:
                num = num//2
            if num in memo:
                memo[originalnum] = ans + memo[num]
                return ans + memo[num]
            else: 
                ans += 1
        return ans
    best = 1
    beststartingnum = 1
    for i in range(1, 1000000):
        currlen = findCollatzLen(i)
        if currlen > best:
            best = currlen
            beststartingnum = i
    print(best, beststartingnum)

start = time()
main()
print('Program took %.02f seconds' % (time()-start))