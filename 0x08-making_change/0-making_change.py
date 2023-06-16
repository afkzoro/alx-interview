#!/usr/bin/python3
""" Fewest Coins """


def makeChange(coins, total):
    """ makeChange function
    summary: Calculates the fewest number of coins
             needed for a given amount total.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    coins.sort(reverse=True)  # Sort coins in descending order

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break  # No need to consider smaller coins since they won't fit

    return dp[total] if dp[total] != float('inf') else -1
