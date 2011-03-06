#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# In England the currency is made up of pound and pence,
# and there are eight coins in general circulation:
# 
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
# 
#   1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can £2 be made using any number of coins?
from itertools import *
def ways_to_change(currencies, amount):
    for r in range(amount+1):
        for c in combinations_with_replacement(currencies, r):
            if sum(c) == amount:
                yield c

def number_of_ways_to_change(currencies, amount):
    pass

def main():
    currencies = (1, 2, 5, 10, 20, 50, 100, 200)
    print(len(set(ways_to_change(currencies, 30))))

if __name__ == "__main__":
    main()
