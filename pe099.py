from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
with open("p099_base_exp.txt", "r") as f:
    a = f.read().split('\n')

# b = [(int(i), int(j)) for pair in a for i, j in pair.split(',')]
# We get a cryptic "ValueError: too many values to unpack (expected 2)"
# because it tries to assign i, j = '519432' and there are more
# characters than there are variables.
#
# This can be fixed a number of ways:
# b = [(int(i), int(j)) for pair in a for i, j in [pair.split(',')]]
# b = [[int(x) for x in pair.split(',')] for pair in a]
b = [list(map(int, pair.split(','))) for pair in a]

#  log is monotonic and log X^Y = Y log X
bestlog, bestrow = max((y*log(x), i) for i, (x, y) in enumerate(b, 1))
print(bestrow)


b = []
for pair in a:
    base, exp = pair.split(',')
    b.append((int(base), int(exp)))

def main():
    def sci(base, exp):
        originalbase = base
        originalpower = 0
        while originalbase >= 10:
                originalbase /= 10
                originalpower += 1
        #print(originalbase, originalpower)
        currpower = originalpower
        currbase = originalbase
        while exp > 1:
            currbase *= originalbase
            currpower += originalpower
            if currbase >= 10:
                currbase /= 10
                currpower += 1
            exp -= 1

        return currbase, currpower

    bestline = 0
    bestbase = 0
    bestpower = 0

    for i, pair in enumerate(b,1):
        base, exp = sci(pair[0], pair[1])
        if exp > bestpower or (exp == bestpower and base > bestbase):
            bestline = i
            bestbase = base
            bestpower = exp
        
    return bestline





start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))