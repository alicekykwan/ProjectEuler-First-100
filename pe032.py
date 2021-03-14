from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from math import *
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written 
as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def main():
    a = (list(permutations([i for i in range(1,10)])))
    ans = set()
    def listtonum(lst):
        ans = 0
        for num in lst:
            ans *= 10
            ans += num
        return ans
    for p in a:
        for i in range(1, 7): #first chunk can go up to 7
            for j in range(i+1, 8): #second chunk goes from i to 8
                n1 = listtonum(p[:i])
                n2 = listtonum(p[i:j])
                n3 = listtonum(p[j:])
                a, b, c = sorted([n1,n2,n3])
                if a*b == c:
                    ans.add(c)
    
    print(ans)


def other():
    found = set()
    for a in range(10**4):
        for b in range(a):
            c = a * b
            s = '%d%d%d' % (a, b, c)
            if len(s) > 9: break
            if len(s) < 9: continue
            if set(s) == set('123456789'):
                print('%d x %d = %d' % (a, b, c))
                found.add(c)
    print(sum(found))



start = time()
other()
print('Program took %.02f seconds' % (time()-start))
    
start = time()
main()
print('Program took %.02f seconds' % (time()-start))