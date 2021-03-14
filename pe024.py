
from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
'''
https://en.wikipedia.org/wiki/Factorial_number_system
'''

def main():
    fact = [1]
    for i in range(1, 10): fact.append(fact[-1] * i)
    n = 10**6 - 1
    a = [i for i in range(10)]
    ans = []
    choices = 9
    while n:
        nextdigit = n//fact[choices]
        
        ans.append(a[nextdigit])
        
        a.remove(a[nextdigit])
        
        n -= nextdigit*fact[choices]
        choices -= 1
    
    ans += a
    print(ans)
    
    n = 10**6 - 1
    a = permutations([i for i in range(10)])
    for _ in range(n): next(a)
    print(next(a))



start = time()
main()
print('Program took %.02f seconds' % (time()-start))