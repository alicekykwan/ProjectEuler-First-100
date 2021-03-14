
from collections import *
from itertools import *
from random import *
from time import *
from functools import *

'''
The nth term of the sequence of triangle numbers is given by, 
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?

'''

f = open("p042_words.txt", "r")
a = f.read()
f.close()


a = a.split(",")
a.sort()
words = []
for word in a:
    words.append(word.strip("\""))

def main():
    def wordvalue(word):
        value = 0
        for letter in word:
            value += ord(letter)-ord("A")+1
        return value
    maxscore = max(len(word) for word in words) * 26
    tnums = [1]
    curr = 2
    while tnums[-1] < maxscore:
        tnums.append(curr*(curr+1)//2)
        curr += 1
    tnums = set(tnums)
    
    print (sum(1 for word in words if wordvalue(word) in tnums))

    

start = time()
main()
print('Program took %.02f seconds' % (time()-start))