"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible (divisible with no
remainder) by all of the numbers from 1 to 20?
"""

def smallest_multiple(limit):
    """Find the smallest positive number that is evenly divisible by all of the
    numbers from 1 to the provided limit.

    Seconds to execute 100 times when finding the LCM of 1 to 10: 0.187355995178.
    """
    multiple = 1
    lcm_found = False
    while not lcm_found:
        for factor in range(1, limit + 1):
            # Check if the multiple is not evenly divisible by the current factor.
            if multiple % factor != 0:
                multiple += 1
                break

            if factor == limit:
                lcm_found = True

    return multiple


def get_prime_factorization(number):
    """Create a dictionary containing the provided number's prime factorization."""
    prime_factorization = {}
    # Inline sieve of Erastothenes; starting at 2 ensures factors will only be prime.
    for factor in range(2, number + 1):
        if number % factor == 0:
            # Record the number of times this factor is contained in the number.
            exponent = 0
            while number % factor == 0:
                number /= factor
                exponent += 1

            prime_factorization[factor] = exponent

            # Check if we've factored the number completely.
            if number == 1:
                return prime_factorization


def smallest_multiple_improved(limit):
    """Find the smallest positive number that is evenly divisible by all of the
    numbers from 1 to the provided limit by computing the product of that
    number's prime factorization.

    Seconds to execute 100 times when finding the LCM of 1 to 10: 0.00209903717041.
    Seconds to execute 100 times when finding the LCM of 1 to 20: 0.00543713569641. Crazy!
    """
    prime_factors = {}
    for factor in range(2, limit + 1):
        prime_factorization = get_prime_factorization(factor)
        for factor, exponent in prime_factorization.items():
            if factor not in prime_factors:
                prime_factors[factor] = exponent
            else:
                if exponent > prime_factors[factor]:
                    prime_factors[factor] = exponent

    least_common_multiple = 1
    for factor, exponent in prime_factors.items():
        least_common_multiple *= factor**exponent

    return least_common_multiple
