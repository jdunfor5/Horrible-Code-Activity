def calculate(num1, num2, calculation):
    total = 0 #sets the total to 0

    if calculation == "+":
        total = total + num1 #adds num1 to total
        total = total + num2 #adds num2 to total

    elif calculation == "-":
        total = num1 #sets total to num1
        total = total - num2 #subtracts num2 from total

    elif calculation == "/":
        total = num1 #sets total to num1
        total = total / num2 #divides total by num2

    elif calculation == "*":
        total = num1 #sets total to num1
        total = total * num2 #multiplies total by num2
    else:
        return "Issue has occurred" #return a message
    return total #return total

print(calculate(1, 2, "+"))
print(calculate(1, 2, "-"))
print(calculate(1, 2, "/"))
print(calculate(1, 2, "*"))