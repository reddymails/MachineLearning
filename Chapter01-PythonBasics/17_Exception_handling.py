
########
#
#  Exception Handling.
#
########


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("You cannot divide by zero! =")
    print(e)

except ValueError  as e:
    print("Please enter valid numbers!=")
    print(e)

finally:
    print("Program finished.")