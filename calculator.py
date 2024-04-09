"""
Project 1: Basics of Python(Datacamp)
Date: April 7, 2024 
Basic Calculator Program:

Create a simple calculator program that can perform addition, subtraction, multiplication, and division.
Implement error handling to deal with invalid inputs.
Use functions to organize the calculator operations.
"""

def addition(numInput1, numInput2):
    return numInput1 + numInput2

def subtraction(numInput1, numInput2):
    return numInput1 - numInput2

def multiplication(numInput1, numInput2):
    return numInput1 * numInput2

def division(numInput1, numInput2):
    return numInput1 / numInput2 if numInput2 != 0 else "Cannot divide by zero"

def menu():
    print("MENU".center(30, "-"))
    print("Press".ljust(30, " "))
    print("[1]".ljust(22, ".") + "Addition".rjust(3))
    print("[2]".ljust(22, ".") + "Subtraction".rjust(3))
    print("[3]".ljust(22, ".") + "Multiplication".rjust(3))
    print("[4]".ljust(22, ".") + "Division".rjust(3))

def calculator(operator):
    if operator >= 1 and operator <= 4:
        try:
            numInput1 = float(input("\nEnter number: "))
            numInput2 = float(input("Enter another number: "))

            if operator == 1:
                answer = addition(numInput1, numInput2)
            elif operator == 2:
                answer = subtraction(numInput1, numInput2)
            elif operator == 3:
                answer = multiplication(numInput1, numInput2)
            else:
                answer = division(numInput1, numInput2)

            print("Answer: ", answer)
        except ValueError:
            print("Invalid Input! Please enter a valid number.")
    else:
        print("Invalid Input. Only 1 to 4!")

def tryAgain():
    while True:
        print("Do you want to calculate again?")
        choice = input("Press Y if 'Yes', N if 'No': ").upper()
        if choice in ['Y', 'N']:
            return choice
        else:
            print("Invalid input! Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    is_loop = True

    while is_loop:
        menu()
        operator = int(input("Operator: "))
        calculator(operator)

        choice = tryAgain()
        if choice == 'N':
            is_loop = False

