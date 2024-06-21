#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """
    Helper function to check if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determine the winner after x rounds given an array of numbers.
    Return the name of the player that won the most rounds.
    If the winner cannot be determined, return None.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        n = nums[i]
        primes_count = sum(1 for num in range(1, n + 1) if is_prime(num))
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
