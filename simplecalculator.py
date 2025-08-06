# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Simple Calculator")
print("------------------")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose operation: +, -, *, /")
        op = input("Enter operation: ")

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation!")
            continue

        print(f"Result: {result}")

        cont = input("Do you want to perform another operation? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting calculator. Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter numbers only.")
