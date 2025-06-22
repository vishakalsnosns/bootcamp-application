"""
Converts a list of digits to a single number without casting or conversion.

Explanation:
- a number, such as 8351, is made up of 8000+300+50+1.
- store the output as 0 initially.
- for each digit from the left, multiply it by 10 to the power of some exponent.
- for 8351, the leftmost digit x should be 3, which is the length, 4, minus 1.
- x needs to go from 3 to 2 to 1 to 0, therefore subtract 1 for each iteration of the loop.
- add each base 10 number procedurally and then print it.
"""

digits = [8,3,5,1]
#digits = [1, 1, 1, 1]
#digits = [9, 1, 4, 5, 1, 2, 5, 6, 3, 1, 4]

output = 0

length = len(digits)
for i, digit in enumerate(digits):
    exp = length - (i+1)

    output += digit * 10**(exp)

print(output)