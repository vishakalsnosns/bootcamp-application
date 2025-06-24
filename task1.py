"""
Converts a list of digits to a single number without casting or conversion.

Explanation:
- a number, such as 8351, is made up of 8000+300+50+1.
- overall strategy is to add up each digit multiplied by a base 10 exponent corresponding to its position.

- reverse the list so that the 0th exponent comes first (10^0 is 1); corresponding to 1st position.
- as i increases in the for loop, it corresponds to the base ten exponent incrementally.
"""

def Solution(digits):
    digits.reverse()

    output = 0

    length = len(digits)
    for i, digit in enumerate(digits):
        output += digit * 10**(i)

    return output


digits = [8,3,5,1]
# digits = [1, 1, 1, 1]
# digits = [9, 1, 4, 5, 1, 2, 5, 6, 3, 1, 4]

print(Solution(digits))