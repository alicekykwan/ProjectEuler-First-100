from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
def main():
    cubes = [i*i*i for i in range(10000)]
    cubeset = set(cubes)
    cubecounter = []
    for cube in cubes:
        cubecounter.append(Counter(list(str(cube))))
    for i, cube in enumerate(cubecounter):
        pers = 0
        for cube2 in cubecounter:
            if cube == cube2:
                pers += 1
        if pers == 5:
            return (i, i*i*i)
    
    return "not found"

def other():
    d = defaultdict(list)
    for i in range(10**4):
        d[''.join(sorted(str(i**3)))].append(i**3)
    return min(min(v) for _, v in d.items() if len(v)==5)

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))

start = time()
print('\n\n')
print(other())
print('Program took %.02f seconds' % (time()-start))