### part one

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
totalDistance = 0
for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])
    totalDistance += distance

# print the answer
print("Total distance between lists:", totalDistance)

### part two

# calculate similarity scores
totalSimilarity = 0
for i in range(len(list1)):
    hitCount = 0
    for j in range(len(list2)):
        if list2[j] == list1[i]:
            hitCount += 1
    totalSimilarity += list1[i] * hitCount

# print the answer
print("Similarity score between lists:", totalSimilarity)