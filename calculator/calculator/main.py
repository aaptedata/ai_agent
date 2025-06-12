def calculate(expression):
    parts = expression.split()
    if len(parts) != 3:
        return "Invalid expression"

    try:
        num1 = float(parts[0])
        operator1 = parts[1]
        num2 = float(parts[2])

        if operator1 == '*':
            return num1 * num2
        elif operator1 == '/':
            if num2 == 0:
                return "Division by zero"
            return num1 / num2
        elif operator1 == '+':
            return num1 + num2
        elif operator1 == '-':
            return num1 - num2
        else:
            return "Invalid operator"

    except ValueError:
        return "Invalid input"

if __name__ == "__main__":
    expression = input("Enter expression: ")
    result = calculate(expression)
    print(result)
