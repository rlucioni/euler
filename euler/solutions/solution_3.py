"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import sys

from ..utilities import timed_execution


def sieve_of_eratosthenes(limit):
    """Find all prime numbers up to the given limit.

    This is a lazy implementation of the sieve of Eratosthenes.
    """
    # Initialize a list of primality flags for candidate numbers.
    primality_flags = [True]*limit

    # Zero and one are not prime.
    primality_flags[0] = primality_flags[1] = False
    
    for candidate, is_prime in enumerate(primality_flags):
        # Find the next number left marked as prime.
        if is_prime:
            yield candidate
            # Enumerate multiples of the current prime and mark them as
            # not prime (i.e., composite). We can optimize Eratosthenes' method
            # by starting enumeration from the square of the current candidate
            # instead of from the candidate itself, since all multiples of the
            # candidate below its square will already have been visited.
            for multiple in xrange(candidate**2, limit, candidate):
                primality_flags[multiple] = False


def largest_prime_factor(number):
    """Find the largest prime factor of the given number.

    This approach works, but the sieve generator starts running into
    space/memory constraints when given large numbers (like 600851475143).
    """
    primes = sieve_of_eratosthenes(number)

    for prime in primes:
        # Check if the current prime is a factor of the given number.
        while number % prime == 0:
            # Divide number by current prime.
            number /= prime

        # Check if we've just divided by the largest prime.
        if number == 1:
            return prime


def largest_prime_factor_improved(number):
    """Find the largest prime factor of the given number."""
    for candidate in xrange(2, number):
        # Extract as many of the current factor as we can from
        # the number. This approach essentially applies Eratosthenes'
        # method inline! Since we start with 2, the first and smallest
        # prime, only primes will be able to successfully factor the
        # given number. This means we don't need to generate a huge
        # array in which to store primality flags.
        while number % candidate == 0:
            # Divide number by current prime.
            number /= candidate

        # Check if we've just divided by the largest prime.
        if number == 1:
            return candidate


number = int(sys.argv[1])

# Seconds to execute 1000 times when finding the largest factor of 13195: 1.23636722565
# timed_execution.timed_execution(largest_prime_factor, number)

# Seconds to execute 1000 times when finding the largest factor of 13195: 0.00467586517334
# Seconds to execute 1000 times when finding the largest factor of 600851475143: 0.826802968979 <- crazy!
timed_execution.timed_execution(largest_prime_factor_improved, number)
