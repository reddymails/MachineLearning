#
# Variables - Exercise
# Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
# Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see**.**
# Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years**.**
# and usee of double slash ,mode operator etc

pi = 22/7
print(pi)
print(type(pi))
P = 5000
T = 3
R = 3.5
simple_interest = P * T * R
print(simple_interest)
print(type(simple_interest))

#Area of Triangle.
height = 10
base = 15
print(type(base))
area =1/2 *  base * height
print(area)
print(type(area))

#Floor dvision
print(10/3)
## Double slash will eliminate any float numbers and acts like floor() function
print(10//3)
# Mod operator
print(15%4)

print("Trying scientific notation")
print(2.3e4) # prints 23000.0 (23 * 10 to the power 4)
print(2.3e-4) # prints 23/10 to power 4 (i.e .00023)

product = 23.5 * 24.4
print(product)
print(round(product)) # Round truncates any decimals

# Treat the below like Strings
food = "123.45"
drinks = "20.5"
print(food+drinks) # it concatenated rather than adding as numbers.
print(type(food+drinks))

## Formats as Binary number.
print(format(5,'b'))

## Exponent example.
exponent_example = 3 ** 4
print("Exponent="+ str(exponent_example))

operator_precedence  = (10 + 2) * 3
print(operator_precedence)
# Python uses J for representing imaginary part like 4 + 3i
test =4+3J
print(test)
