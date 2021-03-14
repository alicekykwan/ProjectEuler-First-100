from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

with open("p089_roman.txt", "r") as f:
    a = f.read().split('\n')

print(len(a))
print(a[0])
'''
chop into groups
detect descending groups - already subtractive

if the group can be improved (into subtractive style):
can be improved:
IIII into IV
VIIII into IX

XXXX into XL
LXXXX into XC

CCCC into CD
DCCCC into CM

'''
def chop(s):
    improvement = 0
    allowedprev = {"I": "V", "X":"L", "C":"D"}
    groups = groupby(s)
    grouplist = []
    for k, g in groups:
        grouplist.append(list(g))
    n = len(grouplist)
    for i, group in enumerate(grouplist):
        currchar = group[0]
        m = len(group)
        if m == 4 and currchar != "M":
            if i > 0:
                if grouplist[i-1][0] == allowedprev[currchar]:  #check for 9, 90, 900
                    improvement += 3
                else:
                    improvement += 2
            else:
                improvement += 2
    return improvement
    

def main():
    print('HELLO WORLD')
    ans = 0
    for roman in a:
        ans += chop(roman)
    return ans

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))
'''
717 wrong
'''