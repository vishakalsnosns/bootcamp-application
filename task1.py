digits = [8,3,5,1]

output = 0

length = len(digits)
for i, digit in enumerate(digits):
    exp = length - (i+1)

    output += digit * 10**(exp)

print(output)