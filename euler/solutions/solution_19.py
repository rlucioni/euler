"""Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import calendar


MONTHS = 12
SUNDAY = 6


def get_first_sundays(low_year, high_year):
    """
    Find the number of Sundays falling on the first of the month between low_year
    and high_year, inclusive.
    """
    first_sundays = 0

    for year in range(low_year, high_year + 1):
        for month in range(1, MONTHS + 1):
            first_day, _ = calendar.monthrange(year, month)

            if first_day == SUNDAY:
                first_sundays += 1

    return first_sundays
