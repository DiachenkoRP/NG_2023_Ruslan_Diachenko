# UI code
uiBorder = "=" * 48

# Main code
listOfElements = []

print(uiBorder)
print("ATTENTION!!! Enter '.stop' to stop entering...")
print(uiBorder)

counter = 1
while True:
    inputElement = input(f"Enter {counter} element: ")
    if inputElement == '.stop': break
    listOfElements.append(inputElement)
    counter += 1

listOfUniqueElements = []
for element in listOfElements:
    if listOfElements.count(element) == 1:
        listOfUniqueElements.append(element)

print(uiBorder)
print( "List of unique elements:\n", listOfUniqueElements)
print(uiBorder)
