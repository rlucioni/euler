"""Sum square difference

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def sum_square_difference(ceiling):
    """Compute the difference between the sum of squares and the square of
    the sum of the natural numbers up to and including the provided ceiling.
    """
    numbers = range(ceiling + 1)

    sum_squares = sum(map(lambda number: number**2, numbers))
    square_sum = sum(numbers)**2

    sum_square_difference = square_sum - sum_squares

    return sum_square_difference
