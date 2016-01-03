"""Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from euler import utils


def lattice_routes(dimension):
    # Must take `dimension * 2` steps, of which `dimension` must be down.
    return utils.choose(dimension * 2, dimension)
