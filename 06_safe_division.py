try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divided = num1/num2
except ZeroDivisionError:
    print("Cannot divide by Zero.")
except ValueError:
    print("Has to be a number.")