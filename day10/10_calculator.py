def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
              "+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
}


def calculator():
    num1 = int(input("What is the first number?: "))
    should_continue = True

    while should_continue:
        for key in operations:
            print(key)
        operator = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))

        calculate = operations[operator]
        answer = calculate(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()