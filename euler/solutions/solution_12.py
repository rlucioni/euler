"""Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers.

The 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1, 3
6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import math


def triangle_number_generator():
    """Generator yielding the sequence of triangle numbers."""
    i = 0
    while True:
        i += 1
        yield int(i * (i + 1) / 2)


def check_divisors(target):
    """Return the value of the first triangle number to have greater than the target number of divisors."""
    triangles = triangle_number_generator()

    for triangle in triangles:
        divisors = 0

        for i in range(1, int(math.sqrt(triangle) + 1)):
            if triangle % i == 0:
                divisors += 1

                if i*i != triangle:
                    divisors += 1

        if divisors > target:
            return triangle


def check_divisors_alternate(target):
    """Return the value of the first triangle number to have greater than the target number of divisors.

    Uses prime factorizations. Any integer N can be expressed as

        N = p_0^a_0 + p_1^a_1 + ... + p_n^a_n,

    where p_n is a distinct prime number and a_n is its exponent. The number of divisors D(N) of any integer
    N can be computed as

        D(N) = (a_0 + 1) * (a_1 + 1) * ... * (a_n + 1)
    """
    triangles = triangle_number_generator()

    for triangle in triangles:
        divisors = 1
        number = triangle

        for candidate in range(2, triangle):
            exponent = 0

            while number % candidate == 0:
                exponent += 1
                number /= candidate

            divisors *= exponent + 1

            if divisors > target:
                return triangle

            if number == 1:
                break
