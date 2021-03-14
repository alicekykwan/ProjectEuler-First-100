from collections import *
from time import *

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def main():
    ans = 0
    for i in range(100,1000):
        for j in range(100, 1000):
            num = i*j
            numstr = str(num)
            if numstr == numstr[::-1]:
                ans = max(ans, num)
    print(ans)


start = time()
main()
print('Program took %.02f seconds' % (time()-start))