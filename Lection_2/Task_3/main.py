numberListOfSets = 3    # for many sets of data :)
listOfSets = []

# Enter sets of data
for index in range(numberListOfSets):
    setOfData = input(f"Enter set of data[{index + 1}] (divide data by ',' ): ")
    if setOfData == ".stop": break
    listOfSets.append(setOfData.replace(" ", "").split(","))

# Unique editor
uniqueSet = []
for index in range(numberListOfSets):
    uniqueSet.extend(listOfSets[index])

print(f"Set of unique elements by {numberListOfSets} sets of data:\n", list(set(uniqueSet)))
