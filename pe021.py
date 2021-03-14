from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, 
then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def main():
    def properdivisorsum(num):
        divisors = set()
        divisors.add(1)
        i = 2
        while i*i <= num:
            if num%i == 0:
                divisors.update([i, num//i])
            i += 1
        return sum(divisors)
    
    amicable = set()
    for i in range(1, 10000):
        a = properdivisorsum(i) # a = properdivisorsum(220) = 284
        b = properdivisorsum(a) # b = properdivisorsum(284) = 220
        if a != b == i:
            amicable.add(i)
        
    print(sum(amicable))




start = time()
main()
print('Program took %.02f seconds' % (time()-start))