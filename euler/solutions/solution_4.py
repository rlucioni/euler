"""Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys

from ..utilities import timed_execution


def largest_palindromic_product(digits):
    """Find the largest palindrome made from the product of two numbers, each
    with the provided number of digits.
    """
    palindrome_product = None
    lower_limit = 10**(digits - 1)
    upper_limit = 10**digits

    for outer in xrange(lower_limit, upper_limit):
        for inner in xrange(lower_limit, upper_limit):
            # Optimize by avoiding redundant calculations.
            if inner < outer:
                continue

            product = outer*inner
            # Check if the product is a palindrome.
            if str(product)[::-1] == str(product):
                if product > palindrome_product:
                    palindrome_product = product

    return palindrome_product


digits = int(sys.argv[1])

timed_execution.timed_execution(largest_palindromic_product, digits)
