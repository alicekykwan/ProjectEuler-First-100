from collections import *
from itertools import *
from random import *
from time import *

'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def main():
    # every triple looks like k(m^2-n^2), 2kmn, k(m^2+n^2)
    # where gcd(m, n) = 1 and m%2 != n%2
    # perimeter is 2km(m+n) = 1000
    # Find some m(m+n) | 500.  m=4 n=1
    # 8, 15, 17 scaled up
    print(8*15*17*(25**3))

    for a in range(1, 501):
        for b in range(1, a+1):
            c = 1000 - a - b
            if a*a+b*b==c*c:
                print(a*b*c)

start = time()
main()
print('Program took %.02f seconds' % (time()-start))