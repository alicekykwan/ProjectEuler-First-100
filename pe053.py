from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
'''
def main():
    f = [1, 1]
    for i in range(2, 101):
        f.append(f[-1]*i)
    ans = 0
    for i in range(2,101):
        for j in range(1, i):
            if f[i]//(f[j]*f[i-j]) > 1000000:
                ans += 1
    print(ans)

start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))