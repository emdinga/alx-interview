#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """Determine the winner of each round"""
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        """If the number of primes is odd, Maria wins; otherwise, Ben wins"""
        winner = 'Maria' if prime_count % 2 != 0 else 'Ben'
        wins[winner] += 1

    """ Determine the player with the most wins"""
    if wins['Maria'] == wins['Ben']:
        return None
    return max(wins, key=wins.get)


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

