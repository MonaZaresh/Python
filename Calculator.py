def show_menu():
    print("\nWelcome to the Python Calculator! 🧮")
    print("Please choose an operation:")
    print("1. ➕ Add")
    print("2. ➖ Subtract")
    print("3. ✖️ Multiply")
    print("4. ➗ Divide")
    print("5. ❌ Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That's not a number. Try again.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Thanks for using the calculator. Goodbye! 👋")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = num1 + num2
            symbol = "+"
        elif choice == '2':
            result = num1 - num2
            symbol = "-"
        elif choice == '3':
            result = num1 * num2
            symbol = "×"
        elif choice == '4':
            if num2 == 0:
                print("You can't divide by zero!")
                continue
            result = num1 / num2
            symbol = "÷"

        print(f"\n🎉 Result: {num1} {symbol} {num2} = {result}")
    else:
        print("Invalid choice. Please select a number from 1 to 5.")
