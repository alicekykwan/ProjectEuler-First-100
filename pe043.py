from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
def main():
    print('HELLO WORLD')
    zerotonine = [i for i in range(10)]
    pers = permutations(zerotonine)

    def check(per):
        #two = per[1:4]
        if per[3] % 2: return False
        #three = per[2:5]
        if sum(per[2:5]) % 3: return False
        #five = per[3:6]
        if per[5] != 5 and per[5] != 0: return False
        #seven = per[4:7]
        if (per[4]*100 + per[5]*10 + per[6]) % 7: return False
        #eleven = per[5:8]
        if (per[5]*100 + per[6]*10 + per[7]) % 11: return False
        #thirteen = per[6:9]
        if (per[6]*100 + per[7]*10 + per[8]) % 13: return False
        #seventeen = per[7:10]
        if (per[7]*100 + per[8]*10 + per[9]) % 17: return False
        return True
    
    def makeint(per):
        ans = 0
        for digit in per:
            ans *= 10
            ans += digit
        return ans 
    ans = 0
    for per in pers:
        if check(per):
            ans += makeint(per)
    print(ans)

def other():
    '''
    def perm(i):
        if i == n:
            print(a)
            return
        for j in range(i, n):
            a[i], a[j] = a[j], a[i]
            perm(i+1)
            a[i], a[j] = a[j], a[i]
    '''
    n = 10
    a = list(range(n))
    restrictions = [1, 1, 1, 17, 13, 11, 7, 5, 3, 2, 1, 1, 1, 1]
    answer = [0]
    def dfs(i, three, total):
        # remaining = a[i:] =               1 0 4
        # selected  = a[:i] = 9 8 2 7 5 3 6 ....
        #                                  i^ ^j
        # total = ...6357289
        # three = ...635 (divisible by 5)
        #
        # After selecting 1:
        # remaining = a[i:] =                 0 4
        # selected  = a[:i] = 9 8 2 7 5 3 6 1 ....
        #                                     ^i
        # total = ...16357289
        # three = ...163 (not divisible by 3, backtrack)
        #
        # After selecting 0:
        # remaining = a[i:] =                 1 4
        # selected  = a[:i] = 9 8 2 7 5 3 6 0 ....
        #                                     ^i
        # total = ...06357289
        # three = ...063 (divisible by 3)
        if three % restrictions[i] != 0:
            return
        if i == n:
            answer[0] += total
            return
        for j in range(i, n):
            a[i], a[j] = a[j], a[i]
            dfs(i+1, 100*a[i] + three//10, total + a[i]*10**i)
            a[i], a[j] = a[j], a[i]
    dfs(0, 0, 0)
    print(answer[0])

start = time()
print('\n\n')
#print(main())
print('Program took %.02f seconds' % (time()-start))

start = time()
print('\n\n')
print(other())
print('Program took %.02f seconds' % (time()-start))