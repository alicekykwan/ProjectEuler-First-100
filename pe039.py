from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from math import *
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

def main():
    def generatesides(p):
        solutions = set()
        half = ceil(p/2)
        for i in range(half):
            for j in range(half):
                if i + j < half: continue
                k = p-i-j
                a, b, c = sorted([i, j, k])
                if a*a + b*b == c*c:
                    solutions.add((a,b,c))
        return len(solutions)
    
    best = 0
    bestp = 0

    for i in range(4, 1001):
        l = generatesides(i)
        if l > best:
            best = l
            bestp = i

    print(bestp, best)

'''
3 sides are m^2-n^2, 2mn, m^2+n^2
perimeter = 2m^2+2mn = 2m(m+n)
m and n have different parity
m and n are relatively prime to each other
'''
def other(limit=1000):
    c = Counter()
    for m in count(1):
        if 2*m*(m+1) > limit: break
        for n in range(1, m):
            p = 2*m*(m+n)
            if p > limit: break
            if m%2 == n%2: continue
            if gcd(m, n) > 1: continue
            for i in range(p, limit+1, p): c[i] += 1
    print(c.most_common(1))


start = time()
main()
print('Program took %.02f seconds' % (time()-start))

start = time()
other()
other(10**6)
print('Program took %.02f seconds' % (time()-start))