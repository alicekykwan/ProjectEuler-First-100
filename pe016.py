from collections import *
from itertools import *
from random import *
from time import *


'''
What is the sum of the digits of the number 2**1000?
'''


def main():
    num = 2**1000
    ans = 0
    while num:
        ans += num%10
        num //= 10
    print(ans)
start = time()
main()
print('Program took %.02f seconds' % (time()-start))