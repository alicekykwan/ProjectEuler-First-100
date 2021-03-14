from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve
'''
with open("p096_sudoku.txt", "r") as f:
    a = f.read().split('Grid')
'''

pnums = [1]
pentnums = [0]

def pentagonal():
    for k in count(1):
        yield (k*(3*k-1))//2
        yield (k*(3*k+1))//2

i = pentagonal()

def p(n):
    while pentnums[-1] < n:
        pentnums.append(next(i))
    pentnums.append(next(i))
    ans = 0
    j = 1
    #print(pentnums, n, j)
    while pentnums[j] <= n:
        if j % 2:
            k = (j+1)//2
        else:
            k = j//2
        #print(j,k)
        if len(pnums) < n-pentnums[j]:
            p(n-pentnums[j])
        ans += (((-1)**(k+1))*pnums[n-pentnums[j]])%10**6
        j += 1
        #print(pentnums, n, j)

    pnums.append(ans%10**6)
    return pnums[-1]
'''    
    for _ in range(10):
        print(next(i))
    nextpentagonal = next(i)
    if nextpentagonal >= n: 
    '''
    

def main():
    print('HELLO WORLD')
    for a in count(1):
        if a%10000==0: print(a)
        if p(a) % 10**6 == 0:
            return a
    #print(pentnums)
    #print(pnums)




start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))