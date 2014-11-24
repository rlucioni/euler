"""Utility for executing and timing functions."""
import timeit


DEFAULT_LOOPS = 1000


def timing_wrapper(function, *args, **kwargs):
    """Turn a function with arguments into a function without arguments.

    This decorator is best used in conjunction with timeit.timeit.
    """
    def wrapped_function():
        return function(*args, **kwargs)
    
    return wrapped_function


def timed_execution(function, *args, **kwargs):
    """Time the execution of a function with the provided arguments.

    Starts by executing the provided function once, printing the output, then
    timing the function and printing a message about its performance.
    """
    # Python 2.x doesn't allow default keyword arguments to be used after variable
    # length positional and/or keyword arguments. We can get around this by manually
    # popping any expected default keyword arguments out of kwargs.
    loops = kwargs.pop('loops', DEFAULT_LOOPS)

    print "Solution: {solution}".format(solution=function(*args, **kwargs))

    wrapped = timing_wrapper(function, *args, **kwargs)
    execution_time = timeit.timeit(wrapped, number=loops)
    print "Seconds to execute {loops} times: {execution_time}".format(
        loops=loops,
        execution_time=execution_time
    )
