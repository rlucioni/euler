"""Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from euler.solutions import solution_3


def prime_sum(limit):
    """Compute the sum of all primes below the given limit.

    Arguments:
        limit (int): The limit below which primes should be considered.

    Returns:
        int: The sum of all primes below the limit.
    """
    total = 0
    for prime in solution_3.sieve_of_eratosthenes(limit):
        total += prime

    return total
