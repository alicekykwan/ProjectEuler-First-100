from collections import *
from itertools import *
from random import *
from time import *


'''
What is the value of the first triangle number 
to have over five hundred divisors?
'''


def main():
    def numdivisors(num):
        divisors = set([1, num])
        i = 2
        while i*i <= num:
            if num%i == 0:
                divisors.add(i)
                divisors.add(num//i)
            i += 1
        return len(divisors)

    '''
    1+2+3...+n = nth triangle number
    if n is even:
        triangle number = (n+1)*(n//2)
    if n is odd:
        triangle number = (n+1)*(n//2) + n//2 +1
    n*(n+1)//2
    5 * 6 // 2
    6 * 2 + 2 + 1
    '''
    def maketnum(n):
        return n*(n+1)//2
        if n%2 == 0:
            return (n+1)*(n//2)
        else:
            return (n+1)*(n//2) + n//2 + 1
    
    i = 1
    while True:
        tnum = maketnum(i)
        if numdivisors(tnum) > 500:
            print(tnum)
            break
        i += 1

start = time()
main()
print('Program took %.02f seconds' % (time()-start))