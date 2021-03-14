from collections import *
from itertools import *
from random import *
from time import *
from functools import *
from fractions import *
from math import *

#from pe_lib import PrimeSieve

'''

'''

from enum import IntEnum
class PokerHand(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FLOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class Card:
    RANKS = '  23456789TJQKA'
    def __init__(self, card):
        rank, suit = card
        self.rank = Card.RANKS.index(rank)
        self.suit = suit
    def __str__(self):
        return f'{Card.RANKS[self.rank]}{self.suit}'
    def __eq__(self, other): return self.rank == other.rank
    def __ne__(self, other): return self.rank != other.rank
    def __lt__(self, other): return self.rank < other.rank
    def __gt__(self, other): return self.rank > other.rank
    def __le__(self, other): return self.rank <= other.rank
    def __ge__(self, other): return self.rank >= other.rank


def score(hand):
    hand.sort(reverse=True)
    ranks = Counter(card.rank for card in hand)

    # Compute Straight
    straight_highest = None
    if len(ranks) == 5 and max(ranks) - min(ranks) == 4:
        straight_highest = max(ranks)
    if set(ranks) == set([14, 2, 3, 4, 5]):
        straight_highest = 5

    # Compute Flush
    is_flush = len(set(card.suit for card in hand)) == 1

    # Royal Flush and Straight FLush
    if straight_highest is not None and is_flush:
        if straight_highest == 14:
            return PokerHand.ROYAL_FLUSH, straight_highest
        return PokerHand.STRAIGHT_FLUSH, straight_highest

    # Four of a Kind
    for rank, freq in ranks.items():
        if freq == 4:
            other = [card for card in hand if card.rank != rank]
            return PokerHand.FLOUR_OF_A_KIND, rank, other

    # Full house
    for rank1, freq1 in ranks.items():
        if freq1 != 3: continue
        for rank2, freq2 in ranks.items():
            if freq2 != 2: continue
            return PokerHand.FULL_HOUSE, rank1, rank2

    # Flush
    if is_flush:
        return PokerHand.FLUSH, hand

    # Straight
    if straight_highest is not None:
        return PokerHand.STRAIGHT, hand

    # Three of a Kind
    for rank, freq in ranks.items():
        if freq == 3:
            other = [card for card in hand if card.rank != rank]
            return PokerHand.THREE_OF_A_KIND, rank, other

    # Two Pairs
    for rank1, freq1 in ranks.items():
        if freq1 != 2: continue
        for rank2, freq2 in ranks.items():
            if freq2 != 2 or rank1 == rank2: continue
            if rank1 < rank2: rank1, rank2 = rank2, rank1
            other = [card for card in hand if card.rank not in (rank1, rank2)]
            return PokerHand.TWO_PAIRS, rank1, rank2, other

    # One Pair
    for rank, freq in ranks.items():
        if freq == 2:
            other = [card for card in hand if card.rank != rank]
            return PokerHand.ONE_PAIR, rank, other

    # High Card
    return PokerHand.HIGH_CARD, hand

def main():
    with open('p054_poker.txt', 'r') as f:
        a = f.read()
    player1wins = 0
    for row in a.split('\n'):
        cards = [Card(i) for i in row.split(' ')]
        hand1 = cards[:5]
        hand2 = cards[5:]
        '''
        print(', '.join(str(card) for card in hand1) +
              ' ; ' +
              ', '.join(str(card) for card in hand2))
        '''
        score1 = score(hand1)
        score2 = score(hand2)
        if score1 > score2:
            player1wins += 1
    print(player1wins)




start = time()
print('\n\n')
print(main())
print('Program took %.02f seconds' % (time()-start))