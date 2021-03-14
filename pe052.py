from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *


'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def main():
    for i in range(1,7):
        print(i/7.)
    for i in count(1):
        c = Counter(str(i))
        if all(Counter(str(i*j))==c for j in range(2,7)):
            print(i)
            break


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))