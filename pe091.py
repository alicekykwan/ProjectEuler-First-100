from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

def isRightTri(x1,y1,x2,y2):
    l1 = x1*x1 + y1*y1
    l2 = x2*x2 + y2*y2
    l3 = abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2)

    a,b,c = sorted([l1,l2,l3])
    return a+b == c

print(isRightTri(0,1,1,0))


def main():
    print('HELLO WORLD')
    count = 0
    seen = set()
    n = 50
    for x in range(n+1):
        for y in range(n+1):
            for xx in range(x, n+1):
                for yy in range(y+1):
                    if (x == 0 and y ==0) or (xx == 0 and yy == 0): continue
                    if x == xx and y == yy: continue
                    if isRightTri(x,y,xx,yy): 
                        count += 1
    return count



start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))