
from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def main():
    f = [0, 1]
    for i in range(2,10):
        f.append(i**5)

    def digits(num):
        d = []
        while num:
            d.append(num%10)
            num//=10
        return d
    def sumoffifthpower(digits):
        s = 0
        for d in digits:
            s += f[d]
        return s
    res = []
    for i in range(2, 1000000):
        if i == sumoffifthpower(digits(i)):
            res.append(i)
    
    print(res)
    print(sum(res))


start = time()
main()
print('Program took %.02f seconds' % (time()-start))