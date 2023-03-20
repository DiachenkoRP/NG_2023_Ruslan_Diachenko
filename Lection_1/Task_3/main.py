#Main code
firstNum = float(input("Enter first number: "))
secondNum = float(input("Enter second number: "))
operation = input("Attention! There is additional operations (pow, sqrt, %).You can use them also.\nEnter operation (+, -, *, /): ")

match operation:
    #Base operations
    case '+':
        result = firstNum + secondNum
    case '-':
        result = firstNum - secondNum
    case '*':
        result = firstNum * secondNum
    case '/':
        if secondNum != 0:
            result = firstNum / secondNum
        else:
            print("[Error] Division by ZERO!")
    #Additional operations
    case 'pow':
        result = firstNum ** secondNum
    case 'sqrt':
        result = firstNum ** (1/secondNum)
    case '%':
        result = firstNum % secondNum

#Result
print(f"Result: {firstNum} {operation} {secondNum} = {result}")
    
