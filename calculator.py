def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

while True:
    # Menu for the user
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Calculator exiting. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))

    elif choice == '2':
        print("Result: ", sub(num1, num2))

    elif choice == '3':
        print("Result: ", mul(num1, num2))

    elif choice == '4':
        print("Result: ", div(num1, num2))
