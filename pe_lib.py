from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *


class Matrix:
    '''
    mat1 = Matrix([[0,1],[1,1]], M)
    mat2 = Matrix([[1,0],[0,1]], M)
    mat3 = mat1*mat2
    mat4 = mat1**(n-1)
    print(mat1)
    '''
    def __init__(self, arr, modulus):
        self.R = len(arr)
        self.C = len(arr[0])
        self.M = modulus
        self.arr = arr

    @staticmethod
    def identity(size, modulus):
        ans = [[0]*size for _ in range(size)]
        for i in range(size):
            ans[i][i] = 1
        return Matrix(ans, modulus)

    def __str__(self):
        return '%s (mod %d)' % (str(self.arr), self.M)

    def __iter__(self):
        return iter(self.arr)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, i):
        return self.arr[i]

    def __setitem__(self, i, val):
        self.arr[i] = val

    def __add__(self, other):
        assert other.R == self.R and other.C == self.C and other.M == self.M
        ans = [[0]*self.C for _ in range(self.R)]
        for r in range(self.R):
            for c in range(self.C):
                ans[r][c] = (self.arr[r][c] + other.arr[r][c]) % self.M
        return Matrix(ans, self.M)

    def __sub__(self, other):
        assert other.R == self.R and other.C == self.C and other.M == self.M
        ans = [[0]*self.C for _ in range(self.R)]
        for r in range(self.R):
            for c in range(self.C):
                ans[r][c] = (self.arr[r][c] - other.arr[r][c]) % self.M
        return Matrix(ans, self.M)

    def __mul__(self, other):
        assert other.R == self.C and other.M == self.M
        ans = [[0]*other.C for _ in range(self.R)]
        for r in range(self.R):
            for c in range(other.C):
                entry = 0
                for k in range(other.R):
                    entry += self.arr[r][k]*other.arr[k][c]
                ans[r][c] = entry % self.M
        return Matrix(ans, self.M)

    def __pow__(self, n):
        assert self.R == self.C
        currpow = self
        ans = Matrix.identity(self.R, self.M)
        for i in range(self.R):
            ans.arr[i][i] = 1
        while n:
            if n&1 == 1:
                ans = (ans * currpow) 
            n >>= 1
            currpow = (currpow * currpow) 
        return ans


def memoize(fn):
    cache = {}
    def _inner(*args):
        if args in cache:
            return cache[args]
        res = cache[args] = fn(*args)
        return res
    return _inner

@memoize
def binomial(n, m):
    if m==0 or m==n:
        return 1
    if m<0 or m>n:
        return 0
    return binomial(n-1, m) + binomial(n-1, m-1)


def sqrt(n):
    assert 0<=n<1e20
    x = int(n**.5 + .5)
    if x*x>n: x-=1
    return x

def cbrt(n):
    assert abs(n)<1e20
    x = int(n**(1./3) + .5)
    if x*x*x > n: x -= 1
    return x


# pow(12319214,123412341234,23421342341234)
def powermod(a, b, m):
    # returns (a**b) % m
    # O(log b) via binary lifting
    # a^11 = a * a * ... * a
    #        a^1 * a^2 * a^8
    # a^2 = a*a
    # a^4 = a^2 * a^2
    # a^8 = a^4 * a^4
    # 2^101
    # 101 = 1 + 4 + 32 + 64
    # 2^101 = 2^1 * 2^4 * 2^32 * 2^64
    currpow = a
    ans = 1
    while b:
        if b&1 == 1:
            ans = (ans * currpow) % m
        b >>= 1
        currpow = (currpow * currpow) % m
    return ans


class PrimeSieve:
    def __init__(self, n):
        self.n = n
        self.sieve = sieve = [True]*n
        sieve[0] = sieve[1] = False
        for p in range(2, n):
            if p*p>n: break
            if not sieve[p]: continue
            for i in range(p*p, n, p): sieve[i] = False
        self.primes=[i for i in range(2,n) if sieve[i]]

    def isprime(self, x):
        if x < self.n:
            return self.sieve[x]
        for p in self.primes:
            if p * p > x: return True
            if x % p == 0: return False
        if x < self.n * self.n: return True
        raise Exception(f'cannot safely determine if {x} is prime')

    def factor(self, x):
        prime_factors = PrimeFactors()
        for prime in self.primes:
            if x%prime: continue
            multiple = 0
            while x%prime == 0:
                x //= prime
                multiple += 1
            prime_factors[prime] = multiple
            if prime*prime > x: break
        if x >= self.n * self.n:
            raise Exception(f'cannot safely factor {x}')
        if x > 1: prime_factors[x] = 1
        return prime_factors


class PrimeFactors:
    def __init__(self, n=None):
        # factors[p] == a means p^a is a factor.
        self.factors = Counter()
        if n is not None:
            # Note: This is slow.
            # Use PrimeSieve or FactorSieve instead.
            assert n > 0
            for prime in count(2):
                if n%prime: continue
                multiple = 0
                while n%prime == 0:
                    n //= prime
                    multiple += 1
                self.factors[prime] = multiple
                if prime*prime > n: break
            if n > 1: self.factors[n] = 1

    def __str__(self):
        result = []
        for prime, multiple in sorted(self.factors.items()):
            if multiple == 1: result.append(f'{prime}')
            elif multiple > 1: result.append(f'{prime}^{multiple}')
        return ' * '.join(result) if result else '1'

    def __iter__(self):
        return iter(self.factors.items())

    def __getitem__(self, key):
        return self.factors.get(key, 0)

    def __setitem__(self, key, val):
        self.factors[key] = val

    def num_divisors(self):
        i = 1
        for multiple in self.factors.values():
            i *= (multiple+1)
        return i

    def divisors(self):
        d = [1]
        for prime, multiple in self.factors.items():
            nextd = d.copy()
            for i in range(1, multiple+1):
                for prevd in d:
                    nextd.append(prevd*prime**i)
            d = nextd
        return sorted(d)

    def sum_divisors(self):
        i = 1
        for prime, multiple in self.factors.items():
            if multiple == 1: i *= prime + 1
            elif multiple == 2: i *= prime*prime + prime + 1
            elif multiple > 2: i *= (prime**(multiple+1)-1) // (prime-1)
            '''
            curr = 1
            for _ in range(multiple):
                curr = prime*curr + 1
            i *= curr
            '''
        return i

    def totient(self):
        num = 1
        for prime, multiple in self.factors.items():
            if multiple == 1: num *= prime-1
            elif multiple == 1: num *= (prime-1)*prime
            elif multiple > 1: num *= (prime-1) * prime**(multiple-1)
        return num


class FactorSieve:
    def __init__ (self, limit = 10**6):
        # smpr[i] := smallest prime dividing i
        smpr = self.smpr = list(range(limit))
        for p in range(2, limit):
            if p * p >= limit: break
            if smpr[p] < p: continue
            for q in range(p*p, limit, p):
                if smpr[q] == q: smpr[q] = p

    def factor(self, n):
        prime_factors = PrimeFactors()
        while n > 1:
            pd = self.smpr[n]
            prime_factors.factors[pd] += 1
            n //= pd
        return prime_factors


class Fenwick:
    '''
    get(i) finds sum of first i elements;  O(log n)
    increment(i, v) adds v to the ith element;  O(log n)
    initially all elements are 0
    '''
    def __init__(self, n):
        self.f = [0] * (n+1)

    def get(self, i):
        ans = 0
        while i > 0:
            ans += self.f[i]
            i -= i&-i
        return ans

    def increment(self, i, v):
        i += 1
        while i < len(self.f):
            self.f[i] += v
            i += i&-i