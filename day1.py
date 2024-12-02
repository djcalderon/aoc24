# initialize two lists to hold location IDs
list1 = list(())
list2 = list(())

# read in two list contents from file
for line in open("inputs/day1.txt", "r"):
    locations = line.split()
    list1.append(int(locations[0]))
    list2.append(int(locations[1]))

# make sure both lists are equal length
if len(list1) != len(list2):
    print("List lenghts are not equal!")
    exit(1)

# sort the lists numerically ascending
list1.sort()
list2.sort()

# sum up the distances between each pair of list items
sumOfDistances = 0
for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])
    sumOfDistances += distance

# print the answer
print(sumOfDistances)