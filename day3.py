import re

sumOfProducts = 0

for line in open("inputs/day3.txt", "r"):
    # find all valid mul instructions within the input line
    mulInstructions = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", line)
    for i in mulInstructions:
        # isolate the two factors for this mul operation
        factors = re.findall("\\d{1,3}", i)
        # multiply factors and add product to running sum
        sumOfProducts += int(factors[0]) * int(factors[1])

print("Sum of all products:", sumOfProducts)