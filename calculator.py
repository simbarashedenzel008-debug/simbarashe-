def simple_calculator():
    print("=== Simple Calculator ===")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid choice. Please select 1–4.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

simple_calculator()