# Beside ANSI-escape
colorRed = u'\u001b[31m'
colorGreen = u'\u001b[32m'
endColor = u'\u001b[0m'

#Main code
firstNum = float(input(f"Enter {colorGreen}first number: {endColor}"))
secondNum = float(input(f"Enter {colorGreen}second number: {endColor}"))
operation = input(f"{colorRed}Attention!{colorGreen} There is additional operations (pow, sqrt, %). You can use them also.{endColor}\nEnter {colorGreen}operation (+, -, *, /){endColor}: ")

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
            print(f"{colorRed}[Error] Division by ZERO!{endColor}")
            exit()
    #Additional operations
    case 'pow':
        result = firstNum ** secondNum
    case 'sqrt':
        result = firstNum ** (1/secondNum)
    case '%':
        result = firstNum % secondNum

#Result
print(f"Result: {colorGreen}{firstNum} {operation} {secondNum} = {result}{endColor}")
    
