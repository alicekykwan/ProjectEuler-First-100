from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
The decimal number, 
585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, 
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, 
may not include leading zeros.)
'''

def main():
    def tobinary(num):
        b = []
        while num:
            b.append(num%2)
            num//=2
        return b
    def isPalin(l):
        n = len(l)
        for i in range(n//2):
            if l[i] != l[n-i-1]:
                return False
        return True
    
    ans = 0
    for i in range(1, 1000000):
        if isPalin(tobinary(i)) and isPalin(list(str(i))):
            ans += i
    print(ans)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))