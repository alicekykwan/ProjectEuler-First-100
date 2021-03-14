from collections import *
from time import *

def main():
    ans = []
    a = 1
    b = 2
    ans.append(b)
    while a + b <= 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            ans.append(b)

    print(ans, sum(ans))


start = time()
main()
print('Program took %.02f seconds' % (time()-start))