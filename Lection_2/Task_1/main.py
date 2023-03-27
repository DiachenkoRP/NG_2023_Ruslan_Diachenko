# UI code
uiBorder = '=' * 48

# Main code

print(uiBorder)
print("Welcome to program that search count elements by user(You) entered!")
listOfData = []
print("Attention! Enter '.stop' to stop entering...")
print(uiBorder)

counter = 0
while True:
    inData = input(f"Enter element[{counter + 1}]: ")
    if inData == '.stop': break
    listOfData.append(inData)
    counter += 1

print(uiBorder)

searchAmount = input("Amount of which element is intrested You?\nEnter: ")
print(f"Amount '{searchAmount}' in you entered elements is ", listOfData.count(searchAmount))
