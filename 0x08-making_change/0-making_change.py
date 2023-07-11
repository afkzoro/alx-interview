#!/usr/bin/python3
""" Fewest Coins """
import time


def makeChange(coins, total):
    """ makeChange function
    summary: Calculates the fewest number of coins
             needed for a given amount total.
    """

    if total <= 0:
        return 0

    # Initialize an dynamic programming array
    # to store the fewest number of coins needed for each total

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all possible totals from 1 to 'total'
    delay = 0.01
    for i in range(1, total + 1):
        # Iterate through all available coin denominations
        for coin in coins:
            if i - coin >= 0:

                # Update the fewest number of coins needed
                # if using this coin leads to a smaller value
                dp[i] = min(dp[i], dp[i - coin] + 1)
                time.sleep(delay)

    # If the fewest number of coins for the total is still infinity
    # it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
