"""10,001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""
import sys
import solution_5

from ..utilities import timed_execution


def find_nth_prime(n):
    """Find the nth prime number by computing prime factorizations.

    If an upper bound for the target prime were known in advance, using a sieve
    of Eratosthenes would be more efficient.
    """
    primes_found = 0
    candidate = 2

    while primes_found < n:
        # All primes except 2 are odd. As such, we can optimize this solution
        # by discarding even numbers which aren't equal to 2.
        if candidate % 2 == 0 and candidate != 2:
            candidate += 1
            continue

        # Check if the candidate's prime factorization consists only
        # of (1 and) itself.
        if solution_5.get_prime_factorization(candidate) == {candidate: 1}:
            primes_found += 1

            if primes_found == n:
                return candidate

        candidate += 1


if __name__ == '__main__':
    n = int(sys.argv[1])

    timed_execution.timed_execution(find_nth_prime, n, loops=1)
