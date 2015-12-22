"""Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts, the terms are allowed to go above one million.
"""

def collatz_sequence(n):
    length = 1

    # Implementing this recursively would allow memoization, but Python isn't
    # the best language to attempt this in. Doing so causes a RecursionError
    # to be raised. Also of note: using a decorator like `functools.lru_cache`
    # for memoization causes the recursion limit to be reached more quickly.
    # See: http://stackoverflow.com/questions/15239123/maximum-recursion-depth-reached-faster-when-using-functools-lru-cache.
    while n > 1:
        length += 1

        if n%2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1

    return length


def longest_collatz_sequence(ceiling):
    longest_chain = {
        'number': 1,
        'length': 1
    }

    for i in range(ceiling):
        length = collatz_sequence(i)
        if length > longest_chain['length']:
            longest_chain = {
                'number': i,
                'length': length
            }

    return longest_chain
