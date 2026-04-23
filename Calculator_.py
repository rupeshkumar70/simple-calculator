# Simple calculator Project
# This is a simple Calculator project built using Python and Object-Oriented Programming (OOP) concepts.

class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2
    
    def mul(self, num1, num2):
        return num1* num2

    def div(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "you can not divide by zero"


    def squr(self, num1):
        return num1 * 2

    def power(self, num1, num2):
        return power ** power



cal = Calculator()

while True:
    print("\n====== CALCULATOR=====\n",
    "1. ADD\n",
    "2. Substract\n",
    "3. multiply\n",
    "4. Divide\n",
    "5. Square\n",
    "6. power \n ",
    "7. Exit",)

    
    try:
        choice = int(input("Entre Your choice: "))
    except ValueError:
        print("please Entre a valid number ")
        continue

    if choice == 7:
        print("program Ended")
        break
    
    try:
        num1 = float (input("Entre first Number: "))
        num2 = float (input("Entre second Number: "))
    except ValueError:
        print("Invalid number input")
        continue
   

    if choice == 1:
        print("Result = ",cal.add(num1, num2))

    elif choice == 2:
        print("Result =",cal.sub(num1, num2))

    elif choice == 3:
        print("Result =",cal.mul(num1, num2))

    elif choice == 4:
        print("Result =",cal.div(num1, num2))

    elif choice == 5:
        print("Result =",cal.squr(num1))

    elif choice == 6:
        print("Result =",cal.squr(num1, num2))
    else:
        print("Invalid input choice correct input")