from collections import *
from itertools import *
from random import *
from time import *


'''
Find the difference between the 
sum of the squares of the first one hundred natural numbers and the 
square of the sum.
'''


def main():
    sumofsq = 0
    for i in range(1, 101):
        sumofsq += i**2
    sqofsum = 0
    for i in range(1, 101):
        sqofsum += i
    sqofsum **= 2

    print(sqofsum-sumofsq)

start = time()
main()
print('Program took %.02f seconds' % (time()-start))