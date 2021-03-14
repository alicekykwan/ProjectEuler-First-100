
from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from datetime import datetime

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def main():
    ans = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            if datetime(year=i, month=j, day=1).weekday() == 6:
                ans += 1
    print(ans)


start = time()
print('\n')
main()
print('Program took %.02f seconds' % (time()-start))