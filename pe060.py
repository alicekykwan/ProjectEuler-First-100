from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *
from pe_lib import PrimeSieve

'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order 
the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes 
with this property.

Find the lowest sum for a set of five primes for which 
any two primes concatenate to produce another prime.
'''
def main():
    prime_sieve = PrimeSieve(1000000)
    primes = prime_sieve.primes
    isprime = prime_sieve.isprime
    def check(a, b):
        s = str(a)
        t = str(b)
        return isprime(int(s+t)) and isprime(int(t+s))

    '''
    We're thinking we need around 4200 primes
    based on a 2.5% independent success on 10 pairs.

    Approach 1: set a hard limit
    - try all n choose 5 combinations
    - can prune if first 2, 3, 4, don't work
    - if no answer, then increase limit
    - if run too long, then lower limit

    Approach 2: increase limit slowly
    - for each prime, in in increasing order
    - first determine which smaller primes are compatible
    - then see if any cliques can be extended
    - we can't throw away the existing cliques

    How to show this is minimal sum? (optional)
    Take lowest 1-clique and add 4*highest prime considered
    Take lowest 2-clique and add 3*highest prime considered
    Take lowest 3-clique and add 2*highest prime considered
    Take lowest 4-clique and add 1*highest prime considered
    If the minimum of these is larger than the clique we found,
    then the clique we found has minimal sum.
    Otherwise increase the highest prime considered.
    '''

    
    '''
    Existing cliques: {}, {1}, {1, 3}, {1, 3, 4}, {1, 4}, {2}, {3}, {4}
    Add: {}, {1, 5}, {1, 4, 5}, {5}
    root (prefix tree)
        1 ->
            3 ->
                4 -> {}
            4 ->
                5 -> {}
            5 -> {}
        2 -> {}
        3 -> {}
        4 -> {}
        5 -> {}
    for each new prime p ascending:
        find all primes q<p compatible with p
        do a dfs over tree only going down paths where compatible and extend
        if depth hits 5, then we print and stop
    '''
    
    class Node:
        def __init__(self):
            self.children = {}

    cliques = Node()
    stack = []
    best = [float('inf')]
    for p in primes:
        if p >= best[0]: break

        cache = {}
        def is_compatible(q):
            if q not in cache:
                cache[q] = check(p, q)
            return cache[q]

        def dfs(node, curr):
            if len(stack) >= 4:
                best[0] = min(best[0], curr)
                print(stack+[p], curr)
            to_remove = []
            for q, childnode in node.children.items():
                if curr + q >= best[0]:
                    to_remove.append(q)
                    continue
                if is_compatible(q):
                    stack.append(q)
                    dfs(childnode, curr+q)
                    stack.pop()
            for q in to_remove:
                del node.children[q]
            node.children[p] = Node()

        dfs(cliques, p)

# [13, 5197, 5701, 6733, 8389] 26033
# [7, 1237, 2341, 12409, 18433] 34427
# [467, 941, 2099, 19793, 25253] 48553


start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))