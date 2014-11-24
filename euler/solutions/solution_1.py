"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import sys

from ..utilities import execute_and_time


def sum_multiples(ceiling, *factors):
    """Find the sum of all multiples below the ceiling of the provided factors."""
    multiples = []

    for number in xrange(ceiling):
        for factor in factors:
            if number % factor is 0:
                multiples.append(number)

    # Convert the list of multiples to a set to eliminate duplicates
    multiple_sum = sum(set(multiples))
    
    return multiple_sum


ceiling = int(sys.argv[1])
factors = [int(factor) for factor in sys.argv[2:]]

execute_and_time.execute_and_time(sum_multiples, ceiling, *factors)
