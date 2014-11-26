"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with no
remainder) by all of the numbers from 1 to 20?
"""
import sys

from ..utilities import timed_execution


def smallest_multiple(limit):
    """Find the smallest positive number that is evenly divisible by all of the
    numbers from 1 to the provided limit.
    """
    multiple = 1
    lcm_found = False
    while not lcm_found:
        for factor in xrange(1, limit + 1):
            # Check if the multiple is not evenly divisible by the current factor.
            if multiple % factor != 0:
                multiple += 1
                break

            if factor == limit:
                lcm_found = True

    return multiple


limit = int(sys.argv[1])

print smallest_multiple(limit)
