#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.

Given a number n,

write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    """
    steps = 0
    copy_all = 'H'
    past = ''
    if n % 2 == 0:
        for i in range(n) or len(copy_all) < n:
            past += copy_all
            steps += 1
    elif n % 2 != 0:
        past = copy_all
        for i in range(n) or len(copy_all) < n:
            past += past
            steps += 1
    else:
        return steps
    return steps
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
