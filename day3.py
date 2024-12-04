import re

sumOfProducts = 0
mulEnabled = True

for line in open("inputs/day3.txt", "r"):
    # find all valid instructions within the input line
    mulInstructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    for i in mulInstructions:
        # determine what type of instruction this is
        if "do()" in i:
            mulEnabled = True
        elif "don't()" in i:
            mulEnabled = False
        elif "mul(" in i and mulEnabled == True:
            # isolate the two factors for this mul operation
            factors = re.findall("\\d{1,3}", i)
            # multiply factors and add product to running sum
            sumOfProducts += int(factors[0]) * int(factors[1])

print("Sum of all products:", sumOfProducts)