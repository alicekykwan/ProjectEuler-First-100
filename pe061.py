from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''
generate all polygonal numbers in the 4 digit range
search from octagonal numbers(fewest of them)
for each octagonal number, 
    find other polygonal numbers that start with the last two digits

'''
def generatepolygonal():
    #triangles:
    t = []
    for n in range(45,141):
        t.append(n*(n+1)//2)

    #squares
    s = []
    for n in range(32, 100):
        s.append(n**2)
    
    # pentagons
    p = []
    for n in range(26, 82):
        p.append(n*(3*n-1)//2)
    
    # hexagons
    hx = []
    for n in range(23, 71):
        hx.append(n*(2*n-1))
    
    # heptagons
    hp = []
    for n in range(21, 64):
        hp.append(n*(5*n-3)//2)
    
    #octagons
    o = []
    for n in range(19, 59):
        o.append(n*(3*n-2))
    
    return([set(poly) for poly in [t, s, p, hx, hp, o]])


def main():
    t, s, p, hx, hp, o = generatepolygonal()
    def dfs(currnum, ans, stillneed):
        if len(stillneed) == 0:
            if currnum%100 == ans[0]//100:
                return (ans, sum(ans))
            else:
                return None
        cycdigits = currnum%100
        for polylist in stillneed:
            for num in polylist:
                if num//100 == cycdigits:
                    newans = ans.copy()
                    newans.append(num)
                    newstillneed = stillneed.copy()
                    newstillneed.remove(polylist)
                    #print(len(newstillneed))
                    res = dfs(num, newans, newstillneed)
                    if res is not None: return res
        return None

    for onum in o:
        res = dfs(onum, [onum], [t,s,p,hx,hp])
        if res: print(res)


# Return the n-th d-polygonal number
def polygonal(d, n):
    return n * ((d-2)*n + 4-d) // 2

# Returns all d-polygonal numbers in [a, b)
def polygonal_between(d, a, b):
    for n in count():
        x = polygonal(d, n)
        if x < a: continue
        if x >= b: break
        yield x

# Whether a ends with first two digits of b
def connects(a, b):
    return a%100 == b//100

def other():
    selected = []
    def find_chain(pos, avail):
        if pos == len(avail):
            return connects(selected[-1], selected[0])
        for num in avail[pos]:
            if pos==0 or connects(selected[-1], num):
                selected.append(num)
                if find_chain(pos+1, avail): return True
                selected.pop()
        return False

    all_polygonal = [set(polygonal_between(d, 1000, 10000)) for d in range(3, 9)]
    for x in permutations(all_polygonal):
        if find_chain(0, x):
            print(selected, sum(selected))
            break

start = time()
print('\n\n')
print(main())
print(other())
print('Program took %.02f seconds' % (time()-start))