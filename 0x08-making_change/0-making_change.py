#!/usr/bin/python3
""" macking changes"""


def makeChange(coins, total):
    """
    determining the fewest number of coins needed 
    to meet a given amount total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
