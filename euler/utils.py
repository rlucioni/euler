"""Utilities for Project Euler solutions."""
import math
import timeit


def _timing_wrapper(function, *args, **kwargs):
    """Turn a function with arguments into a function without arguments.

    This decorator is best used in conjunction with timeit.timeit.
    """
    def wrapped_function():
        return function(*args, **kwargs)
    
    return wrapped_function


def timed_execution(function, *args, loops=1000, **kwargs):
    """Time the execution of a function with the provided arguments.

    Starts by executing the provided function once, printing the output, then
    timing the function and printing a message about its performance.
    """
    print("Solution: {solution}".format(solution=function(*args, **kwargs)))

    wrapped = _timing_wrapper(function, *args, **kwargs)
    execution_time = timeit.timeit(wrapped, number=loops)
    print("Seconds to execute {loops} times: {execution_time}".format(
        loops=loops,
        execution_time=execution_time
    ))


def product(iterable):
    """Compute the product of the given iterable.

    Arguments:
        iterable (iterable of int or float): Numbers to multiply together.

    Returns:
        int: The product of all numbers contained in the iterable.
    """
    product = iterable[0]
    for number in iterable[1:]:
        product *= number

    return product


def choose(n, k):
    """Compute the binomial coefficient.

    Uses // operator to force integer division.

    Arguments:
        n (int): Possibilities.
        k (int): Unordered outcomes.

    Returns:
        int, the binomial coefficient.
    """
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def deserialize_grid(serialized):
    """Deserialize a serialized grid.

    Arguments:
        serialized (str): Serialized representation of a grid of integers.

    Returns:
        list of map objects, each yielding ints
    """
    return [map(int, row.split()) for row in serialized.split('\n') if row]
