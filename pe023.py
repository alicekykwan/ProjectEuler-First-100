
from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper divisors of 
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though 
it is known that the greatest number that cannot be expressed as 
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as 
the sum of two abundant numbers.
'''

def main():
    def divisors(num):
        d = set([1])
        i = 2
        while i*i <= num:
            if num%i == 0:
                d.add(i)
                d.add(num//i)
            i += 1
        return d
    abundant = set()
    for i in range(1, 28124):
        if sum(divisors(i)) > i:
            abundant.add(i)
    '''
    a = sum up all numbers from 1 to 28123
    go through all abundant numbers, record all pairs into a set
    subtract sum of this set from a
    '''
    allnum = sum(i for i in range(1, 28124))
    twoabundant = set()
    for i in abundant:
        for j in abundant:
            if i+j > 28123: break
            twoabundant.add(i+j)
    print(allnum-sum(twoabundant))


def other():
    n = 28124
    fs = list(range(n+1)) # fs[i] := smallest prime divisor of i
    # initial: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    # sieve 2: 0 1 2 3 2 5 2 7 2 9 2  11 2  13 2  15 2
    # sieve 3: 0 1 2 3 2 5 2 7 2 3 2  11 2  13 2  3  2
    # skip 4: already sieved
    # break on 5, because 5 * 5 > 16
    for i in count(2):
        if i*i>n: break
        if fs[i]<i: continue
        for j in range(i*i,n+1,i):
            if fs[j]==j: fs[j]=i

    def divsum(n):
        pf = Counter()
        while n > 1:
            p = fs[n]
            pf[p] += 1
            n //= p
        r = 1
        # 300 = 2^2 * 3^1 * 5^2
        # sum of divs = (1 + 2 + 4) * (1 + 3) * (1 + 5 + 25)
        #             = 1*1*1 + 1*1*5 + 1*1*25 + 1*3*1 + 1*3*5 + ... + 4*3*25
        for p, a in pf.items():
            r *= (p**(a+1)-1) // (p-1) # 1 + p + ... + p^a = (p^(a+1)-1)/(p-1)
        return r

    abundant = [i for i in range(1, n+1) if divsum(i)-i>i]
    abundant_set = set(abundant)
    def twoabundant(n):
        for i in abundant:
            if i > n: break
            if n-i in abundant_set: return True
        return False
    print(sum(i for i in range(1, n+1) if not twoabundant(i)))


start = time()
main()
print('Program took %.02f seconds' % (time()-start))
start = time()
other()
print('Program took %.02f seconds' % (time()-start))