# Specific Symbols
upIndexTwo = u"\u00B2"
downIndexOne = u"\u2081"
downIndexTwo = u"\u2082"

# Main code
qEquation = f"Ax{upIndexTwo} + Bx + C = 0"
print(qEquation)
qA = float(input(f"Enter element A: "))
qB = float(input(f"Enter element B: "))
qC = float(input(f"Enter element C: "))
qEquationOut = f"{qA}x{upIndexTwo} + {qB}x + {qC} = 0"

qDiscriminant = (qB ** 2) - 4 * qA * qC
qDiscriminantSqrt = qDiscriminant ** (1/2)

if (qDiscriminant > 0):
    qX1 = (-qB + qDiscriminantSqrt) / 2 * qA
    qX2 = (-qB - qDiscriminantSqrt) / 2 * qA
    print(f"Roots of {qEquationOut} is \n\tx{downIndexOne} = {qX1}\n\tx{downIndexTwo} = {qX2}.")
elif (qDiscriminant == 0):
    qX = (-qB) / 2 * qA
    print(f"Root of {qEquationOut} is\n\tx = {qX}.")
else:
    print(f"Quadratic equation {qEquationOut} haven't real roots!")
