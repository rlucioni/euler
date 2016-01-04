"""Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

[3]
[7] 4
2 [4] 6
8 5 [9] 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

Note: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67 is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method!
"""
from euler import utils


SMALL_TRIANGLE = '''
    3
    7 4
    2 4 6
    8 5 9 3
'''

LARGE_TRIANGLE = '''
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


def max_path_sum(serialized):
    """Find the max path sum of the serialized triangle.

    Arguments:
        serialized (str): Serialized representation of a triangle of integers.

    Returns:
        int: Maximum path sum.
    """
    triangle = utils.deserialize_grid(serialized)
    triangle_base_length = len(triangle[-1])
    cache = [[] for row in triangle]

    for row_index, cache_row in enumerate(cache):
        for triangle_row_index in range(row_index, triangle_base_length):
            element = triangle[triangle_row_index].pop()

            # Number of elements remaining in the popped triangle row
            # corresponds to cache column index.
            column_index = len(triangle[triangle_row_index])

            try:
                left = cache_row[column_index - 1]
            except IndexError:
                left = None

            try:
                upper = cache[row_index - 1][column_index]
            except IndexError:
                upper = None

            if left and upper:
                cache_row.append(max(left, upper) + element)
            elif left or upper:
                cache_row.append((left or upper) + element)
            else:
                cache_row.append(element)

    return max([row[-1] for row in cache])
