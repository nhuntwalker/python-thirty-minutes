"""Do whatever math I want to do at a given point in time."""


def add(num1: float, num2: float) -> float:
    """Add two numbers."""
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    """Subtract two numbers."""
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """Multiply two numbers."""
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    """Divide two numbers."""
    return num1 / num2


switchboard = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("ERROR: You didn't provide enough arguments!")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("ERROR: You provided too many arguments!")
        sys.exit(1)

    operation = sys.argv[1]
    if operation not in switchboard:
        print(
            f"ERROR: {operation} isn't a supported operation. Try 'multiply', 'divide', 'add', or 'subtract'"
        )
        sys.exit(1)

    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    result = switchboard[operation](num1, num2)
    print(f"Result: {result}")
