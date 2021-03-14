from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def main():
    primes = [2, 3, 5, 7]
    curr = 9
    ans = []
    def isPrime(num):
        for p in primes:
            if p*p > num: break
            if num%p == 0: return False
        return True
    def trytruncate(num):
        primesSet = set(primes)
        numstr = str(num)
        n = len(numstr)
        tocheck = []
        for i in range(1, n):
            tocheck.append(int(numstr[i:]))
            tocheck.append(int(numstr[:n-i]))
        if all(i in primesSet for i in tocheck):
            ans.append(num)
            return True
        return False
        
    while len(ans) < 11:
        #find the next prime
        foundnextprime = False
        while foundnextprime is False:
            if isPrime(curr):
                foundnextprime = True
                primes.append(curr)
            curr += 2
        candidate = curr-2
        #this filter reduces time for 75sec to 2.4 sec
            #first digit must be 2,3,5,7
            #middle digits must be 1, 3, 7, 9
            #last digit must be 3, 7
        digitsStr = list(str(candidate))
        n = len(digitsStr)
        if digitsStr[0] in '2357' and digitsStr[-1] in '37' and all(digitsStr[i] in '1379' for i in range(1,n-1)):
            #check if it's truncatable
            trytruncate(curr-2)
            #if so, add to ans (did within helper)
        
    print(ans)
    print(sum(ans))

start = time()
main()
print('Program took %.02f seconds' % (time()-start))