from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve
'''
with open(".txt", "r") as f:
    a = f.read().split('\n')
'''

'''
                     pos
Elements: SELECTED... | ...AVAILABLE

Sets: [0,1,2]
'''
groups = [[0,1,2],[3,2,4],[5,4,6],[7,6,8],[9,8,1]]
elements = [10] + list(range(1,10))
results = []
def handle_permutation():
    sums = [sum(elements[i] for i in group) for group in groups]
    if min(sums) == max(sums):
        #print(elements,sums)
        correctdescribe = []
        describe = [elements[i] for group in groups for i in group]
        for _ in range(5):
            describe = describe[3:]+describe[:3] 
            correctdescribe.append(describe)
        results.append(''.join(str(i) for i in min(correctdescribe)))
        
def dfs(pos=1):
    if pos == len(elements):
        handle_permutation()
        return
    for i in range(pos, len(elements)):
        elements[pos], elements[i] = elements[i], elements[pos]
        dfs(pos + 1)
        elements[pos], elements[i] = elements[i], elements[pos]

def main():
    dfs(1)
    print(results)
    return max(results)

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))