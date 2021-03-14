from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Find the sum of the digits in the number 100!
'''


def main():
    def prod(nums):
        return reduce(lambda x, y: x*y, nums, 1)
    a = prod([i for i in range(1, 101)])
    a = str(a)
    ans = 0
    for c in a:
        ans += int(c)
    print(ans)
start = time()
main()
print('Program took %.02f seconds' % (time()-start))