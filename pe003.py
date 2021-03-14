from collections import *
from time import *
from math import ceil
from pe_lib import PrimeFactors

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
def main():
    num = 600851475143
    print(max(PrimeFactors(num))[0])
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            largest = i
    if num > 1:
        largest = num
    print(largest)
    num = 600851475143
    primefactors = set()
    a = 2
    while num:
        if num % a == 0:
            primefactors.add(a)
        while num % a == 0:
            num //= a
        a += 1
        if a**2 > num:
            primefactors.add(num)
            break
    print(primefactors)
    print(max(primefactors))



            


start = time()
main()
print('Program took %.02f seconds' % (time()-start))