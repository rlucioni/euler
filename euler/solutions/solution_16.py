"""Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def power_digit_sum(exponent, base=2):
    # Python automatically switches to bignums when necessary.
    power = base ** exponent
    digits = [int(digit) for digit in str(power)]

    return sum(digits)
