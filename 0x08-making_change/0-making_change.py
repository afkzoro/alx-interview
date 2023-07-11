#!/usr/bin/python3
import time
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

    coins = coins[::-1]  # Reverse the coins list

    # Artificially introduce a delay to slow down the execution
    delay = 0.01
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                time.sleep(delay)

    return dp[total] if dp[total] != float('inf') else -1
