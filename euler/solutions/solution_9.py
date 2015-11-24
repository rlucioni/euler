"""Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_pythagorean_triplet(a, b, c):
    """Determine whether the provided numbers are a Pythagorean triplet.

    Arguments:
        a, b, c (int): Three integers.

    Returns:
        Boolean: True is the provided numbers are a Pythagorean triplet, False otherwise.
    """
    return (a < b < c) and (a**2 + b**2 == c**2)


def pair_sums(total, least):
    """Find all pairs which add up to the provided sum.

    Arguments:
        total (int): Number to which returned pairs must sum.
        least (int): The smallest integer which may be part of a returned pair.

    Returns:
        set of tuples: Containing pairs of integers adding up to the given sum.
    """
    pairs = set()
    for i in range(least, total - least):
        pair = [i, total - i]
        pair.sort()

        pairs |= set([tuple(pair)])

    return pairs


def find_triplet_product(total):
    """Find a Pythagorean triplet adding up to the provided sum.

    Arguments:
        total (int): An integer to which a triplet must sum.

    Returns:
        tuple of list and int: First Pythagorean triplet found and its product.
        None: If no Pythagorean triplet summing to the provided total exists.
    """
    triplets = []

    for i in range(1, total):
        pairs = pair_sums(total - i, i)

        for pair in pairs:
            triplet = [i]
            triplet += pair
            triplets.append(triplet)

    for triplet in triplets:
        a, b, c = triplet

        if is_pythagorean_triplet(a, b, c):
            return triplet, a * b * c
