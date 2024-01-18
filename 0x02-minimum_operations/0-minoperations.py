#!/usr/bin/python3
""" a method that calculates the fewest number of operations
needed to result in exactly n H characters """


def minOperations(n):
    """ find the character H """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
