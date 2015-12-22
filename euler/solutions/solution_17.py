"""Number letter counts

If the numbers 1 to 5 are written out in words:

    one, two, three, four, five

Then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
"""
import inflect


def letter_count(max, min=1):
    """Count the number of letters used to spell the numbers from min to max, inclusive."""
    e = inflect.engine()
    count = 0

    for i in range(min, max + 1):
        words = e.number_to_words(i)
        valid_letters = [letter for letter in words if letter not in (' ', '-')]
        count += len(valid_letters)

    return count
