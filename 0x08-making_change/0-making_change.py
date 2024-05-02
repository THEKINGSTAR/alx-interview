#!/usr/bin/python3
"""
Change comes from within
"""

import collections


def makeChange(coins: list, total: int) -> int:
    """
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total.
    Args:
        coins (list): totoal numbers of coins in pile
        total (int): total chance
    """
    coin_pile = {}
    for coin in coins:
        coin_pile[coin] = 0

    sorted_coins = {k: coin_pile[k] for k in sorted(coin_pile, reverse=True)}
    # print(sorted_coins)
    keys_list = list(sorted_coins.keys())
    k_l_len = len(keys_list)
    i = 0

    while total and i < k_l_len:
        if total >= keys_list[i]:
            total -= keys_list[i]
            sorted_coins[keys_list[i]] += 1
        else:
            i += 1

    chage_sum = sum(sorted_coins.values())

    # print(sorted_coins)
    # print(chage_sum)
    # return sorted_coins

    if total > 0:
        return -1
    else:
        return chage_sum


"""
# Example usage:
coins = [1, 2, 25]  # Coin denominations
total_change = 37  # Total change needed

result = makeChange(coins, total_change)
print("Total number of coins:", result)

coins = [1256, 54, 48, 16, 102]  # Coin denominations
total_change = 1453  # Total change needed

result = makeChange(coins, total_change)
print("Total number of coins:", result)
"""
