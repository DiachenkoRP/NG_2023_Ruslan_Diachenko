def operationWarning():
    print("Avaible operation: +, -, *, /. Also additional operation **, %, sqrt.")
def calculateInfo(num1,num2, operation):
    result = 0
    match userOperation:
        case '+':
            result = add(userNum1, userNum2)
        case '-':
            result = sub(userNum1, userNum2)
        case '*':
            result = mult(userNum1, userNum2)
        case '/':
            result = div(userNum1, userNum2)
        case '**':
            result = power(userNum1, userNum2)
        case 'sqrt':
            result = sqrt(userNum1, userNum2)
        case '%':
            result = mod(userNum1, userNum2)
        case _:
            print("Unknown operation!")
    print(f"Output: {num1} {operation} {num2} = {result}")

def userInputNumber(text):
    x = int(input(text))
    return x
def userInputString(text):
    x = input(text)
    return x
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2
def mult(num1, num2):
    return num1 * num2

def power(base, power):
    return base ** power
def sqrt(base, root):
    return base ** (1/root)
def mod(num1, num2):
    return num1 % num2

# MAIN
userNum1 = userInputNumber("Enter first num: ")
userNum2 = userInputNumber("Enter second num: ")

operationWarning()
userOperation = userInputString("Enter operation: ")

calculateInfo(userNum1,userNum2,userOperation)




