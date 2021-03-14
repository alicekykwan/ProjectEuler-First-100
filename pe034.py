from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the 
sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def main():
    f = [1]
    for i in range(1, 10):
        f.append(f[-1]*i)
    #print(f[9]*7)   #9999999  7 digit numbers can have digit factorial sum of 2540160

    def digitfactorial(num):
        d = []
        while num:
            d.append(num%10)
            num//=10
        ans = 0
        for digit in d:
            ans += f[digit]
        return ans
    ans = 0
    for i in range(3, 2540161):
        if i == digitfactorial(i):
            ans += i
    print(ans)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))