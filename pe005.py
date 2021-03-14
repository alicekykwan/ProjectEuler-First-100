from collections import *
from time import *
from math import gcd

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def main():
    def lcm(a, b):
        return (a*b)//gcd(a,b)

    a = 2   # 1, 2, 3, 4 .... 20  
    b = 2   # LCM of everything up to and including a
    while a < 20:
        a, b = a+1, lcm(a+1, b)
    print(b)
    print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)

start = time()
main()
print('Program took %.02f seconds' % (time()-start))