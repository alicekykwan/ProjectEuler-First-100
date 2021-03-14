from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def main():
    def findremainders2(d):
        remainders = {}
        remainder = 1
        place = 9
        while remainder not in remainders:
            remainders[remainder] = place
            remainder = (10*remainder)%d
            place += 1
        if remainder == 0: return 0
        return place - remainders[remainder]
    def findremainders(d):
        remainders = {}
        currremainder = 1
        place = 1
        while currremainder != 0:
            currremainder*=10
            decimal = currremainder//d
            nextremainder = currremainder - decimal*d
            if nextremainder in remainders:
                return place - remainders[nextremainder]
            remainders[nextremainder] = place
            currremainder = nextremainder
            place += 1
        return 0
    best = 0
    bestd = 0
    for i in range(1,1000):
        if findremainders(i) > best:
            best = findremainders(i)
            bestd = i
    print(bestd)



start = time()
main()
print('Program took %.02f seconds' % (time()-start))