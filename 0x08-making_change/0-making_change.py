#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be met.
    Returns:
        int: The fewest number of coins needed to meet total.
    """
    if total <= 0:
        return 0

    """ Create a list to store the fewest number
    of coins needed for each total
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """ Iterate through each coin value"""
    for coin in coins:
        """ Update the dp list for each total amount"""
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    """ Return the fewest number of coins needed for the given total """
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Example usage
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
