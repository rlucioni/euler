"""Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 (26) 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 (63) 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 (78) 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 (14) 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

GRID = '''
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''


def construct_grid(string_grid):
    """Construct a list of lists representing a grid of integers.

    Arguments:
        string_grid (str): The string representation of the grid, complete with newlines.

    Returns:
        list of list of int: Representing a grid of integers.
    """
    raw_rows = string_grid.split('\n')

    rows = []
    for row in raw_rows:
        if row:
            rows.append(row)

    grid = []
    for row_index, row in enumerate(rows):
        elements = row.split()
        grid.append([])

        for element in elements:
            try:
                grid[row_index].append(int(element))
            except:
                continue

    return grid


# TODO: Move to a utility module.
def product(iterable):
    """Compute the product.

    Arguments:
        iterable (iterable of int): Numbers to multiply together.

    Returns:
        int: The product of all numbers contained in the iterable.
    """
    product = iterable[0]
    for number in iterable[1:]:
        product *= number

    return product


def is_greater(numbers, adjacent, greatest_product):
    """Check if the product of the given numbers is greater than the greatest product.

    Arguments:
        numbers (list of int): A list of numbers to multiply together.
        adjacent (int): The required count of (adjacent) numbers.
        greatest_product (int): The current greatest product.

    Returns:
        int: If the count of numbers is equal to the required value, and the product
            of the numbers is greater than the greatest product.
        None: Otherwise.
    """
    if len(numbers) == adjacent:
        current_product = product(numbers)
        if greatest_product is None or current_product > greatest_product:
            return current_product


# TODO: This could be more cleanly implemented as a class.
def search_grid(grid, adjacent):
    """Search a grid for the greatest product of adjacent numbers.

    Arguments:
        grid (list of list of int): Representation of the grid to search.
        adjacent (int): How many adjacent numbers to consider.

    Returns:
        int: Greatest product of adjacent numbers.
    """
    greatest_product = None

    # We only need to search right, down, and diagonally (upper right and 
    # lower right) as we visit each element to traverse the entire grid.
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            # Look right
            right = row[column_index:column_index + adjacent]

            current_product = is_greater(right, adjacent, greatest_product)
            if current_product is not None:
                greatest_product = current_product

            # Look down
            down = []
            for i in range(adjacent):
                try:
                    down.append(grid[row_index + i][column_index])
                # Index might be out of range, which means there isn't the required
                # count of numbers vertically-adjacent to the current number.
                except:
                    break

            current_product = is_greater(down, adjacent, greatest_product)
            if current_product is not None:
                greatest_product = current_product

            # Look diagonally, upper right
            upper_diagonal = []
            for i in range(adjacent):
                working_row_index = row_index - i

                # We don't want to be using negative indices, which would wrap around to
                # the bottom of the grid.
                if row_index < 0:
                    break

                try:
                    upper_diagonal.append(grid[working_row_index][column_index + i])
                # Index might be out of range, which means there isn't the required
                # count of numbers diagonally-adjacent to the current number.
                except:
                    break

            current_product = is_greater(upper_diagonal, adjacent, greatest_product)
            if current_product is not None:
                greatest_product = current_product

            # Look diagonally, lower right
            lower_diagonal = []
            for i in range(adjacent):
                try:
                    lower_diagonal.append(grid[row_index + i][column_index + i])
                # Index might be out of range, which means there isn't the required
                # count of numbers diagonally-adjacent to the current number.
                except:
                    break

            current_product = is_greater(lower_diagonal, adjacent, greatest_product)
            if current_product is not None:
                greatest_product = current_product

    return greatest_product
