from collections import *
from itertools import *
from random import *
from time import *

def main():
    ans = 0
    for i in range(1000):
        if i%3 == 0 or i%5 == 0:
            ans += i
    print(ans)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))