safeReportCount = 0

for report in open("inputs/day2.txt", "r"):
    levels = [int(level) for level in report.split()]
    safe = True
    increasing = 0
    for i in range(1, len(levels)):
        # check to make sure level is increasing or decreasing
        if levels[i] == levels[i-1]:
            safe = False # stable levels are unsafe
            break
        # check to make sure levels are all increasing or all decreasing
        if i == 1:
            if levels[i] > levels[i-1]:
                increasing = 1
            elif levels[i] < levels[i-1]:
                increasing = -1
        else:
            if levels[i] > levels[i-1] and increasing == -1:
                safe = False; # fluctuating levels are unsafe
                break
            elif levels[i] < levels[i-1] and increasing == 1:
                safe = False; # fluctuating levels are unsafe
                break
        # check to make sure levels are changing gradually
        if abs(levels[i] - levels[i-1]) > 3:
            safe = False; # differences greater than 3 are unsafe
            break
    # is this report safe?
    if safe == True:
        safeReportCount += 1

# print the answer
print("Number of safe reports:", safeReportCount)