def calculate(num1, num2, calculation):
    total = 0 #sets the total to 0

    if calculation == "+":
        total = total + num1 #adds num1 to total
        total = total + num2 #adds num2 to total

    elif calculation == "-":
        total = num1
        total = total - num2

    elif calculation == "/":
        total = num1
        total = total / num2

    elif calculation == "*":
        total = num1
        total = total * num2
    else:
        return "Issue has occurred"
    return total # returns total

print(calculate(1, 2, "+"))
print(calculate(1, 2, "-"))
print(calculate(1, 2, "/"))
print(calculate(1, 2, "*"))