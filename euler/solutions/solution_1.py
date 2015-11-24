"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_multiples(ceiling, *factors):
    """Find the sum of all multiples of the provided factors below the ceiling."""
    multiples = []

    for number in range(ceiling):
        for factor in factors:
            # Check if the current number is a multiple of the current factor.
            if number % factor == 0:
                multiples.append(number)

    # Eliminate duplicate multiples by converting the list of multiples to a set.
    multiple_sum = sum(set(multiples))
    
    return multiple_sum
