from calculator import Calculator

def main():
    calc = Calculator()

    a = float(input("Enter your first value: "))

    b = float(input("Enter your second value: "))

    print("Choose an operation:")
    print("1 - sum: ")
    print("2 - subtract: ")
    print("3 - multiply: ")
    print("4 - divide: ")

    operation = int(input("# "))

    if operation == 1:
        print(calc.sum(a,b))

    if operation == 2:
        print(calc.subtract(a,b))

    if operation == 3:
        print(calc.multiply(a,b))

    if operation == 4:
        print(calc.divide(a,b))


if __name__ == "__main__":
    main()

